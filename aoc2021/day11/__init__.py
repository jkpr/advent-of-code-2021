from itertools import product


def neighbors(i: int, j: int, dim: int) -> tuple[int, int]:
    for d in product([-1, 0, 1], repeat=2):
        if d != (0, 0):
            if (new_i := i + d[0]) in range(dim) and (new_j := j + d[1]) in range(dim):
                yield new_i, new_j


def next_gen(octopuses: dict[tuple[int, int], int], dim: int) -> int:
    flashed = set()
    for i in range(dim):
        for j in range(dim):
            octopuses[(i, j)] += 1
    to_flash = set(k for k, v in octopuses.items() if v > 9)
    while to_flash:
        for point in to_flash:
            for neighbor in neighbors(*point, dim):
                octopuses[neighbor] += 1
            flashed.add(point)
        to_flash = set(k for k, v in octopuses.items() if v > 9) - flashed
    for i in flashed:
        octopuses[i] = 0
    return len(flashed)


def place_octopuses(lines: list[str]) -> dict[tuple[int, int], int]:
    octopuses = {}
    for i, line in enumerate(lines):
        for j, octopus in enumerate(line):
            octopuses[(i, j)] = int(octopus)
    return octopuses


def part1(lines: list[str]):
    octopuses = place_octopuses(lines)
    dim = len(lines)
    counts = []
    for _ in range(100):
        flashed = next_gen(octopuses, dim)
        counts.append(flashed)
    return sum(counts)


def part2(lines: list[str]):
    octopuses = place_octopuses(lines)
    dim = len(lines)
    for i in range(1_000_000):
        flashed = next_gen(octopuses, dim)
        if flashed == dim * dim:
            return i + 1
