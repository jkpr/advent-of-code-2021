from collections import (
    Counter,
    defaultdict,
)
from math import (
    prod,
)


def get_depths(lines) -> dict[tuple[int, int], int]:
    depths = defaultdict(lambda: 9)
    for i, line in enumerate(lines):
        for j, level in enumerate(line):
            depths[(i, j)] = int(level)
    return depths


def part1(lines: list[str]):
    depths = get_depths(lines)
    low_points = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            up = depths[(i - 1, j)]
            down = depths[(i + 1, j)]
            left = depths[(i, j - 1)]
            right = depths[(i, j + 1)]
            if depths[(i, j)] < min(i for i in [up, down, left, right]):
                low_points.append(depths[(i, j)])
    return sum(low_points) + len(low_points)


def expand_basin(
    point: tuple[int, int],
    basin_labels: dict[tuple[int, int], int],
    depths: dict[tuple[int, int], int],
    current: int,
) -> None:
    if point not in basin_labels and depths[point] < 9:
        basin_labels[point] = current
        expand_basin((point[0] + 1, point[1]), basin_labels, depths, current)
        expand_basin((point[0] - 1, point[1]), basin_labels, depths, current)
        expand_basin((point[0], point[1] - 1), basin_labels, depths, current)
        expand_basin((point[0], point[1] + 1), basin_labels, depths, current)


def part2(lines: list[str]):
    depths = get_depths(lines)
    current_label = 0
    basin_labels = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            expand_basin((i, j), basin_labels, depths, current_label)
            current_label += 1
    biggest = Counter(basin_labels.values()).most_common(3)
    return prod(i[1] for i in biggest)
