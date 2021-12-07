def move_crabs(lines: list[str], fuel_cost: callable) -> int:
    crabs = [int(i) for i in lines[0].split(",")]
    total_fuel = []
    for i in range(max(crabs)):
        fuel_for_crab = []
        for crab in crabs:
            fuel_for_crab.append(fuel_cost(i, crab))
        total_fuel.append(sum(fuel_for_crab))
    return min(total_fuel)


def part1(lines: list[str]):
    return move_crabs(lines, lambda i, x: abs(x - i))


def part2(lines: list[str]):
    return move_crabs(lines, lambda i, x: abs(x - i) * (abs(x - i) + 1) // 2)
