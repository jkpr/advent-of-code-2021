from itertools import combinations, product
from re import findall
from typing import Callable, Iterable


Point = tuple[int, int, int]


def rotate_x(point: Point) -> Point:
    return point[0], -point[2], point[1]


def rotate_y(point: Point) -> Point:
    return -point[2], point[1], point[0]


def rotate_z(point: Point) -> Point:
    return -point[1], point[0], point[2]


def all_rotations() -> Iterable[Callable[[Point], Point]]:
    reference = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    seen = set()
    for x, y, z in product(range(4), repeat=3):

        def rotate(point):
            for _ in range(x):
                point = rotate_x(point)
            for _ in range(y):
                point = rotate_y(point)
            for _ in range(z):
                point = rotate_z(point)
            return point

        rotated_reference = tuple(rotate(i) for i in reference)
        if rotated_reference not in seen:
            seen.add(rotated_reference)
            yield rotate


def diffs(points: list[Point]) -> list[Point]:
    return [(j[0] - i[0], j[1] - i[1], j[2] - i[2]) for i, j in zip(points, points[1:])]


def attempt_alignment(
    known_beacons: set[Point], unknown_beacons: list[Point]
) -> tuple[set[Point] | None, Point | None]:
    for axis in range(3):
        known_sorted = sorted(known_beacons, key=lambda p: p[axis])
        unaligned_beacons = sorted(unknown_beacons, key=lambda p: p[axis])
        known_diffs = diffs(known_sorted)
        unaligned_diffs = diffs(unaligned_beacons)
        for matching_diff in set(known_diffs) & set(unaligned_diffs):
            kx, ky, kz = known_sorted[known_diffs.index(matching_diff)]
            ux, uy, uz = unaligned_beacons[unaligned_diffs.index(matching_diff)]
            dx, dy, dz = ux - kx, uy - ky, uz - kz
            aligned_beacons = {
                (x - dx, y - dy, z - dz) for x, y, z in unaligned_beacons
            }
            scanner = -dx, -dy, -dz
            if len(aligned_beacons & known_beacons) >= 12:
                return aligned_beacons, scanner
    return None, None


def find_aligned_beacons_and_scanner(
    known_beacons: set[Point], unknown_scanner_readings: list[set[Point]]
) -> tuple[int, set[Point], Point]:
    for i, scanner_readings in enumerate(unknown_scanner_readings):
        for rotate in all_rotations():
            rotated = [rotate(reading) for reading in scanner_readings]
            aligned, scanner = attempt_alignment(known_beacons, rotated)
            if aligned and scanner:
                return i, aligned, scanner
    raise Exception("Unable to align any beacons")


def align_beacons_and_scanners(
    lines: list[str],
) -> tuple[set[Point], list[Point]]:
    unknown_scanner_readings = []
    chunks = "\n".join(lines).split("\n\n")
    result = [chunk.strip().splitlines() for chunk in chunks]
    for chunk in result:
        readings = set()
        for line in chunk[1:]:
            reading = tuple(int(i) for i in findall(r"-?\d+", line))
            readings.add(reading)
        unknown_scanner_readings.append(readings)
    known_beacons = unknown_scanner_readings.pop(0)
    known_scanners = [(0, 0, 0)]
    for _ in range(len(unknown_scanner_readings)):
        index, beacons, scanner = find_aligned_beacons_and_scanner(
            known_beacons, unknown_scanner_readings
        )
        unknown_scanner_readings.pop(index)
        known_beacons |= beacons
        known_scanners.append(scanner)
    return known_beacons, known_scanners


def part1(lines: list[str]):
    beacons, _ = align_beacons_and_scanners(lines)
    return len(beacons)


def part2(lines: list[str]):
    _, scanners = align_beacons_and_scanners(lines)
    return max(
        abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2])
        for i, j in combinations(scanners, 2)
    )
