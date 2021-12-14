from collections import Counter
from functools import cache

from .utils import get_counts


def simulate_recursive(lines: list[str], times: int) -> int:
    start = list(lines[0])
    rules = dict(line.split(" -> ") for line in lines[2:])

    @cache
    def next_gen_recursive(bigram: str, times: int) -> Counter:
        if times == 0:
            return Counter([bigram])
        middle = rules[bigram]
        left = next_gen_recursive(f"{bigram[0]}{middle}", times - 1)
        right = next_gen_recursive(f"{middle}{bigram[1]}", times - 1)
        return left + right

    counter = sum(
        (next_gen_recursive("".join(i), times) for i in zip(start, start[1:])),
        start=Counter(),
    )
    counts = get_counts(counter, start[0], start[-1])

    print(next_gen_recursive.cache_info())
    return max(counts.values()) - min(counts.values())


def part1(lines: list[str]):
    return simulate_recursive(lines, 10)


def part2(lines: list[str]):
    return simulate_recursive(lines, 40)
