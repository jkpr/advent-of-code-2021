from ..utils import lines_to_int


def part1(lines: list[str]):
    ints = lines_to_int(lines)
    return sum(b > a for a, b in zip(ints, ints[1:]))


def part2(lines: list[str]):
    ints = lines_to_int(lines)
    return sum(
        sum(items[1:]) > sum(items[:-1])
        for items in zip(ints, ints[1:], ints[2:], ints[3:])
    )
