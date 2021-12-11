matches = {
    "{": "}",
    "(": ")",
    "<": ">",
    "[": "]",
}

illegal_char_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

completion_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_illegal_char(line: str) -> str:
    stack = []
    for char in line:
        if char in "{[<(":
            stack.append(char)
        elif stack:
            last = stack.pop()
            if matches[last] != char:
                return char
    else:
        return None


def part1(lines: list[str]):
    scores = []
    for line in lines:
        char = get_illegal_char(line)
        scores.append(illegal_char_points.get(char))
    return sum(filter(None, scores))


def get_completion_string(line: str) -> str:
    stack = []
    for char in line:
        if char in "{[<(":
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(matches[char] for char in reversed(stack))


def get_completion_score(completion: str) -> int:
    score = 0
    for char in completion:
        score = score * 5 + completion_points[char]
    return score


def part2(lines: list[str]):
    scores = []
    for line in lines:
        if get_illegal_char(line) is None:
            completion = get_completion_string(line)
            score = get_completion_score(completion)
            scores.append(score)
    return sorted(scores)[len(scores) // 2]
