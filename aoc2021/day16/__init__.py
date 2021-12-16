from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from math import prod


@dataclass
class Literal:
    start: int
    end: int
    value: int

    @classmethod
    def from_tape(cls, tape: str, i: int) -> Literal:
        start = i
        frames = []
        while i < len(tape):
            this_frame = tape[i : (i + 5)]
            frames.append(this_frame[1:])
            i += 5
            if this_frame[0] == "0":
                break
        end = i
        value = int("".join(frames), base=2)
        return cls(start, end, value)


@dataclass
class Header:
    start: int
    end: int
    version: int
    packet_type: int
    length_type: str = None
    length_value: int = None

    @classmethod
    def from_tape(cls, tape: str, i: int) -> Header:
        start = i
        version = int(tape[i : (i + 3)], base=2)
        packet_type = int(tape[(i + 3) : (i + 6)], base=2)
        if packet_type != 4:
            length_type = tape[i + 6]
            i += 7
            if length_type == "0":
                length_value = int(tape[i : (i + 15)], base=2)
                i += 15
            else:
                length_value = int(tape[i : (i + 11)], base=2)
                i += 11
        else:
            i += 6
            length_type = None
            length_value = None
        end = i
        return cls(start, end, version, packet_type, length_type, length_value)


@dataclass
class Packet:
    start: int
    end: int
    header: Header
    literal: Literal | None
    sub_packets: list[Packet]

    def eval(self) -> int:
        if self.literal:
            return self.literal.value
        match self.header.packet_type:
            case 0:
                return sum(p.eval() for p in self.sub_packets)
            case 1:
                return prod(p.eval() for p in self.sub_packets)
            case 2:
                return min(p.eval() for p in self.sub_packets)
            case 3:
                return max(p.eval() for p in self.sub_packets)
            case 5:
                return 1 if self.sub_packets[0].eval() > self.sub_packets[1].eval() else 0
            case 6:
                return 1 if self.sub_packets[0].eval() < self.sub_packets[1].eval() else 0
            case 7:
                return 1 if self.sub_packets[0].eval() == self.sub_packets[1].eval() else 0

    @classmethod
    def from_tape(cls, tape: str, i: int) -> Packet:
        start = i
        header = Header.from_tape(tape, i)
        i = header.end
        literal = None
        sub_packets = []
        if header.packet_type == 4:
            literal = Literal.from_tape(tape, i)
            i = literal.end
        elif header.length_type == "0":
            until = i + header.length_value
            sub_packets = cls.from_type_until(tape, i, until)
            i = until
        else:
            count = header.length_value
            sub_packets = cls.from_type_count(tape, i, count)
            i = sub_packets[-1].end
        end = i
        return cls(start, end, header, literal, sub_packets)

    @classmethod
    def from_type_until(cls, tape: str, i: int, until: int) -> list[Packet]:
        packets = []
        while i < until:
            packet = Packet.from_tape(tape, i)
            packets.append(packet)
            i = packet.end
        return packets

    @classmethod
    def from_type_count(cls, tape: str, i: int, count: int) -> list[Packet]:
        packets = []
        for _ in range(count):
            packet = Packet.from_tape(tape, i)
            packets.append(packet)
            i = packet.end
        return packets


def part1(lines: list[str]) -> int:
    tape = f"{int(lines[0], base=16):0{len(lines[0]) * 4}b}"
    packet = Packet.from_tape(tape, i=0)
    to_sum = deque([packet])
    sum = 0
    while to_sum:
        next_packet = to_sum.popleft()
        sum += next_packet.header.version
        to_sum.extend(next_packet.sub_packets)
    return sum


def part2(lines: list[str]):
    tape = f"{int(lines[0], base=16):0{len(lines[0]) * 4}b}"
    packet = Packet.from_tape(tape, i=0)
    return packet.eval()
