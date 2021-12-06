from collections import (
    Counter,
)


def spawn_lanternfish(lines: list[str], days: int) -> int:
    ints = [int(i) for i in lines[0].split(",")]
    fish = Counter(ints)
    for _ in range(days):
        next_gen = {k - 1: v for k, v in fish.items() if k != 0}
        next_gen[6] = next_gen.get(6, 0) + fish.get(0, 0)
        next_gen[8] = fish.get(0, 0)
        fish = next_gen
    return sum(fish.values())


def part1(lines: list[str]):
    return spawn_lanternfish(lines, 80)


def part2(lines: list[str]):
    return spawn_lanternfish(lines, 256)
