def part1(lines: list[str]):
    gamma = []
    epsilon = []
    for digits in zip(*lines):
        n_one = sum(i == "1" for i in digits)
        n_zero = len(digits) - n_one
        if n_one > n_zero:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")
    return int("".join(gamma), base=2) * int("".join(epsilon), base=2)


def part2(lines: list[str]):
    oxygen = []
    filtered = lines
    for i in range(len(lines[0])):
        if len(filtered) == 1:
            oxygen = list(filtered[0])
            break
        n_one = sum(line[i] == "1" for line in filtered)
        n_zero = len(filtered) - n_one
        most_common = "1" if n_one >= n_zero else "0"
        oxygen.append(most_common)
        filtered = [line for line in filtered if line[i] == most_common]

    co2 = []
    filtered = lines
    for i in range(len(lines[0])):
        if len(filtered) == 1:
            co2 = list(filtered[0])
            break
        n_one = sum(line[i] == "1" for line in filtered)
        n_zero = len(filtered) - n_one
        least_common = "0" if n_one >= n_zero else "1"
        co2.append(least_common)
        filtered = [line for line in filtered if line[i] == least_common]

    return int("".join(oxygen), base=2) * int("".join(co2), base=2)
