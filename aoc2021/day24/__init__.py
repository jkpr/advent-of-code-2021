def decipher(lines: list[str], maximize: bool):
    result = [0] * 14
    stack = []
    chunk_size = 18
    for i in range(len(lines) // chunk_size):
        instructions = lines[slice(i * chunk_size, (i + 1) * chunk_size)]
        should_push = instructions[4].split()[-1] == "1"
        if should_push:
            push_value = int(instructions[15].split()[-1])
            stack.append([i, push_value])
        else:
            last_index, last_value = stack.pop()
            diff = last_value + int(instructions[5].split()[-1])
            if maximize:
                if diff >= 0:
                    result[i] = 9
                    result[last_index] = 9 - diff
                else:
                    result[i] = 9 + diff
                    result[last_index] = 9
            else:
                if diff >= 0:
                    result[i] = 1 + diff
                    result[last_index] = 1
                else:
                    result[i] = 1
                    result[last_index] = 1 - diff
    return "".join(str(i) for i in result)


def part1(lines: list[str]):
    return decipher(lines, maximize=True)


def part2(lines: list[str]):
    return decipher(lines, maximize=False)
