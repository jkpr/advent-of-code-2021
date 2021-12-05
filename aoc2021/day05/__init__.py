from collections import (
    defaultdict,
)
from re import (
    findall,
)


def count_vents(lines: list[str], diagonals: bool):
    field = defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = [int(i) for i in findall(r"\d+", line)]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                field[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                field[(i, y1)] += 1
        elif diagonals:
            x_delta = 1 if x1 < x2 else -1
            y_delta = 1 if y1 < y2 else -1
            for i in range(abs(x2 - x1) + 1):
                new_x = x1 + x_delta * i
                new_y = y1 + y_delta * i
                field[(new_x, new_y)] += 1
    return sum(v > 1 for v in field.values())


def part1(lines: list[str]):
    return count_vents(lines, diagonals=False)


def part2(lines: list[str]):
    return count_vents(lines, diagonals=True)
