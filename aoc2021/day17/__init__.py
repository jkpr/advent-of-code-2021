from itertools import count
from re import findall


def sum_i(n: int) -> int:
    return n * (n + 1) // 2


def get_start_x(x_min) -> int:
    for n in count():
        if sum_i(n) >= x_min:
            return n


def part1(lines: list[str]) -> int:
    x_min, x_max, y_min, y_max = [int(i) for i in findall(r"-?\d+", lines[0])]
    return (abs(y_min) - 1) * (abs(y_min)) // 2


def trajectory_at_n(dx: int, dy: int, n: int) -> tuple[int, int]:
    x = dx * (dx + 1) // 2 if n > dx else n * dx - (n - 1) * n // 2
    y = n * dy - (n - 1) * n // 2
    return x, y


def trajectory_lands_in_target(
    dx: int,
    dy: int,
    x_min: int,
    x_max: int,
    y_min: int,
    y_max: int,
) -> bool:
    for n in count(start=1):
        x, y = trajectory_at_n(dx, dy, n)
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        elif x > x_max or y < y_min:
            return False


def part2(lines: list[str]) -> int:
    x_min, x_max, y_min, y_max = [int(i) for i in findall(r"-?\d+", lines[0])]
    dx_min = get_start_x(x_min)
    dx_max = x_max
    dy_min = y_min
    dy_max = abs(y_min) - 1
    count = 0
    for dx in range(dx_min, dx_max + 1):
        for dy in range(dy_min, dy_max + 1):
            count += trajectory_lands_in_target(dx, dy, x_min, x_max, y_min, y_max)
    return count
