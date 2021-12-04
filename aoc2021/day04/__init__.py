def get_boards(lines: list[str]) -> list[list[str]]:
    boards = []
    board_strings = "\n".join(lines).strip().split("\n\n")
    for board_string in board_strings:
        board = [line.split() for line in board_string.split("\n")]
        boards.append(board)
    return boards


def get_bingos_for_boards(boards: list[list[str]]) -> list[list[set[str]]]:
    all_bingos = []
    for board in boards:
        bingos = []
        for row in board:
            bingos.append(set(row))
        for col in zip(*board):
            bingos.append(set(col))
        all_bingos.append(bingos)
    return all_bingos


def get_boards_as_sets(boards: list[list[str]]) -> list[set[str]]:
    all_board_sets = []
    for board in boards:
        all_sets = [set(line) for line in board]
        all_board_sets.append(set.union(*all_sets))
    return all_board_sets


def play_bingo(nums: list[str], bingos_for_boards: list[list[str]]) -> dict[int, int]:
    results = {}
    for i in range(1, len(nums) + 1):
        called = set(nums[:i])
        for board_index, bingos in enumerate(bingos_for_boards):
            if any(called & bingo == bingo for bingo in bingos):
                if board_index not in results:
                    results[board_index] = i
    return results


def get_final_score(lines: list[str], func: callable) -> int:
    boards = get_boards(lines[2:])
    bingos_for_boards = get_bingos_for_boards(boards)
    nums = lines[0].split(",")
    results = play_bingo(nums, bingos_for_boards)
    board, count = func(results.items(), key=lambda x: x[1])
    all_board_sets = get_boards_as_sets(boards)
    board_set = all_board_sets[board]
    uncalled = board_set - set(nums[:count])
    return sum(int(i) for i in uncalled) * int(nums[count - 1])


def part1(lines: list[str]) -> int:
    return get_final_score(lines, min)


def part2(lines: list[str]) -> int:
    return get_final_score(lines, max)
