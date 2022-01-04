from itertools import accumulate, combinations
from re import findall, search


def explode(line: str) -> str:
    stack = []
    for i, char in enumerate(line):
        if char == "[":
            stack.append(i)
        elif char == "]":
            if len(stack) > 4:
                start = stack.pop()
                end = i + 1
                first, second = [int(i) for i in findall(r"\d+", line[start:end])]
                if prev_match := search(r"\d+", line[start - 1 :: -1]):
                    prev_start = start - prev_match.end()
                    prev_end = start - prev_match.start()
                    prev_num = int(line[prev_start:prev_end]) + first
                    prev_str = line[:prev_start] + str(prev_num) + line[prev_end:start]
                else:
                    prev_str = line[:start]
                if next_match := search(r"\d+", line[end:]):
                    next_start = end + next_match.start()
                    next_end = end + next_match.end()
                    next_num = int(line[next_start:next_end]) + second
                    next_str = line[end:next_start] + str(next_num) + line[next_end:]
                else:
                    next_str = line[end:]
                return f"{prev_str}0{next_str}"
            stack.pop()
    return line


def split(line: str) -> str:
    if match := search(r"\d{2,}", line):
        start = match.start()
        end = match.end()
        num = int(line[start:end])
        first = num // 2
        second = num // 2 + num % 2
        new_num = f"[{first},{second}]"
        return line[:start] + new_num + line[end:]
    else:
        return line


def reduce(line: str) -> str:
    while True:
        exploded = explode(line)
        if exploded != line:
            line = exploded
            continue
        splitted = split(exploded)
        if splitted != exploded:
            line = splitted
            continue
        return splitted


def add(line1: str, line2: str) -> str:
    added = f"[{line1},{line2}]"
    reduced = reduce(added)
    return reduced


def get_magnitude(final) -> int:
    if isinstance(final, list):
        return 3 * get_magnitude(final[0]) + 2 * get_magnitude(final[1])
    else:
        return final


def part1(lines: list[str]):
    snail_sum = list(accumulate(lines, add))[-1]
    magnitude = get_magnitude(eval(snail_sum))
    return magnitude


def part2(lines: list[str]):
    magnitudes = []
    for line1, line2 in combinations(lines, 2):
        magnitude1 = get_magnitude(eval(add(line1, line2)))
        magnitude2 = get_magnitude(eval(add(line2, line1)))
        magnitudes.append(magnitude1)
        magnitudes.append(magnitude2)
    return max(magnitudes)
