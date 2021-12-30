from itertools import product


def next_gen(
    algo: list[int],
    image: set[tuple[int, int]],
    min_i: int,
    max_i: int,
    min_j: int,
    max_j: int,
    default: int,
) -> set[tuple[int, int]]:
    next_image = set()
    for i, j in product(range(min_i - 1, max_i + 2), range(min_j - 1, max_j + 2)):
        index_bits = (
            int((i + di, j + dj) in image)
            if min_i <= i + di <= max_i and min_j <= j + dj <= max_j
            else default
            for di, dj in product([1, 0, -1], repeat=2)
        )
        index = sum(1 << n if bit else 0 for n, bit in enumerate(index_bits))
        if algo[index]:
            next_image.add((i, j))
    return next_image


def setup(lines: list[str]) -> tuple[list[int], set[tuple[int, int]]]:
    algo = [int(i == "#") for i in lines[0]]
    image = set()
    for i, line in enumerate(lines[2:]):
        for j, char in enumerate(line):
            if char == "#":
                image.add((i, j))
    return algo, image


def enhance_image(lines: list[str], times) -> int:
    algo, image = setup(lines)
    for n in range(times):
        default = 0 if algo[0] == 0 else n % 2
        image = next_gen(
            algo, image, -n, len(lines[2:]) + n, -n, len(lines[2]) + n, default
        )
    return len(image)


def part1(lines: list[str]):
    return enhance_image(lines, 2)


def part2(lines: list[str]):
    return enhance_image(lines, 50)
