from itertools import count


def march_herd(
    mark: str,
    direction: tuple[int, int],
    sea_floor: dict[tuple[int, int], str],
    dim: tuple[int, int],
):
    next_sea_floor = {}
    for (i, j), v in sea_floor.items():
        if v == mark:
            next_space = ((i + direction[0]) % dim[0], (j + direction[1]) % dim[1])
            if sea_floor[next_space] == ".":
                next_sea_floor[(i, j)] = "."
                next_sea_floor[next_space] = mark
    for k, v in sea_floor.items():
        if k not in next_sea_floor:
            next_sea_floor[k] = v
    return next_sea_floor


def march(sea_floor, dim: tuple[int, int]):
    sea_floor = march_herd(">", (0, 1), sea_floor, dim)
    sea_floor = march_herd("v", (1, 0), sea_floor, dim)
    return sea_floor


def part1(lines: list[str]):
    sea_floor = {}
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            sea_floor[(i, j)] = ch
    dim = i + 1, j + 1
    for i in count(1):
        next_sea_floor = march(sea_floor, dim)
        if next_sea_floor == sea_floor:
            return i
        sea_floor = next_sea_floor


def part2(lines: list[str]):
    ...
