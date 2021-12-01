from aoc2021.utils import lines_to_int


def part1(lines: list[str]):
    ints = lines_to_int(lines)
    count = 0
    for a, b in zip(ints, ints[1:]):
        if b > a:
            count += 1
    return count


def part2(lines: list[str]):
    ints = lines_to_int(lines)
    triples = []
    for a, b, c in zip(ints, ints[1:], ints[2:]):
        triples.append(a + b + c)
    count = 0
    for a, b in zip(triples, triples[1:]):
        if b > a:
            count += 1
    return count
