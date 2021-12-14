from collections import Counter, defaultdict

from .utils import get_counts


def next_gen(counter: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    next_gen = defaultdict(int)
    for bigram, count in counter.items():
        middle = rules[bigram]
        one = f"{bigram[0]}{middle}"
        two = f"{middle}{bigram[1]}"
        next_gen[one] += count
        next_gen[two] += count
    return next_gen


def simulate(lines: list[str], times: int) -> int:
    start = list(lines[0])
    rules = dict(line.split(" -> ") for line in lines[2:])
    counter = Counter("".join(i) for i in zip(start, start[1:]))
    for _ in range(times):
        counter = next_gen(counter, rules)
    counts = get_counts(counter, start[0], start[-1])
    return max(counts.values()) - min(counts.values())


def part1(lines: list[str]):
    return simulate(lines, 10)


def part2(lines: list[str]):
    return simulate(lines, 40)
