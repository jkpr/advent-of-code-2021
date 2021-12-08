from collections import defaultdict
from itertools import permutations
from re import findall


source = """
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


def _get_digit_by_segments() -> dict[str, int]:
    segments = defaultdict(set)
    for i, line in enumerate(source.splitlines()):
        for j, char in enumerate(line):
            if char in "abcdefg":
                row = 0 if i < 10 else 1
                col = j // 8
                num = row * 5 + col
                segments[num].add(char)
    return {"".join(sorted(v)): k for k, v in segments.items()}


digit_by_segments = _get_digit_by_segments()


def get_decryption(patterns: list[str]):
    for perm in permutations("abcdefg"):
        d = dict(zip("abcdefg", perm))
        new_patterns = []
        for pattern in patterns:
            new_patterns.append("".join(sorted(d[p] for p in pattern)))
        if set(new_patterns) == set(digit_by_segments):
            return {
                frozenset(old): str(digit_by_segments[new])
                for old, new in zip(patterns, new_patterns)
            }


def part2(lines: list[str]):
    all_nums = []
    for line in lines:
        words = findall(r"\w+", line)
        func = get_decryption(words[:-4])
        num = int("".join(func[frozenset(i)] for i in words[-4:]))
        all_nums.append(num)
    return sum(all_nums)
