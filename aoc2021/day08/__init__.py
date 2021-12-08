from itertools import (
    chain,
)
from re import (
    findall,
)


def part1(lines: list[str]):
    outputs = []
    for line in lines:
        words = findall(r"\w+", line)
        outputs.append(words[-4:])
    return sum(len(item) in (2, 3, 4, 7) for item in chain(*outputs))


def get_signal_map(patterns: list[set[str]]):
    result = {}
    result[1] = next(i for i in patterns if len(i) == 2)
    result[7] = next(i for i in patterns if len(i) == 3)
    result[4] = next(i for i in patterns if len(i) == 4)

    bd = result[4] - result[1]

    for pattern in patterns:
        if len(pattern) == 5:
            if len(pattern & result[1]) == 2:
                result[3] = pattern
            elif len(pattern & bd) == 2:
                result[5] = pattern
            else:
                result[2] = pattern
        elif len(pattern) == 6:
            if len(pattern & bd) == 1:
                result[0] = pattern
            elif len(pattern & result[1]) == 1:
                result[6] = pattern
            else:
                result[9] = pattern
        elif len(pattern) == 7:
            result[8] = pattern
    return result


def part2(lines: list[str]):
    entries = []
    for line in lines:
        words = findall(r"\w+", line)
        signals = words[:-4]
        output = words[-4:]
        entries.append((signals, output))

    output_nums = []
    for signals, output in entries:
        signal_map = get_signal_map([set(i) for i in signals])
        segment_map = {frozenset(v): str(k) for k, v in signal_map.items()}
        output_num = int("".join(str(segment_map[frozenset(i)]) for i in output))
        output_nums.append(output_num)
    return sum(output_nums)
