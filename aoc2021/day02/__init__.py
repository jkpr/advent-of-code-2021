def part1(lines: list[str]):
    depth = 0
    length = 0
    for line in lines:
        parts = line.split()
        direction = parts[0]
        distance = int(parts[1])
        if direction == "forward":
            length += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
    return depth * length


def part2(lines: list[str]):
    aim = 0
    depth = 0
    length = 0
    for line in lines:
        parts = line.split()
        direction = parts[0]
        distance = int(parts[1])
        if direction == "forward":
            length += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return depth * length
