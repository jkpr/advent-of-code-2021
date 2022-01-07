import heapq

"""
PATH_DATA

key: 
    tuple(
        hallway spot,
        room number,
    )

value:
    tuple(
        distance from hallway spot to first spot in room (index 0 of the room), 
        [
            hallway spot that must be open,
            another hallway spot that must be open,
            ...
        ],
    )
"""
PATH_DATA = {
    (0, 0): (3, [1]),
    (0, 1): (5, [1, 2]),
    (0, 2): (7, [1, 2, 3]),
    (0, 3): (9, [1, 2, 3, 4]),
    (1, 0): (2, []),
    (1, 1): (4, [2]),
    (1, 2): (6, [2, 3]),
    (1, 3): (8, [2, 3, 4]),
    (2, 0): (2, []),
    (2, 1): (2, []),
    (2, 2): (4, [3]),
    (2, 3): (6, [3, 4]),
    (3, 0): (4, [2]),
    (3, 1): (2, []),
    (3, 2): (2, []),
    (3, 3): (4, [4]),
    (4, 0): (6, [2, 3]),
    (4, 1): (4, [3]),
    (4, 2): (2, []),
    (4, 3): (2, []),
    (5, 0): (8, [2, 3, 4]),
    (5, 1): (6, [3, 4]),
    (5, 2): (4, [4]),
    (5, 3): (2, []),
    (6, 0): (9, [2, 3, 4, 5]),
    (6, 1): (7, [3, 4, 5]),
    (6, 2): (5, [4, 5]),
    (6, 3): (3, [5]),
}


"""
ROOM_TO_ROOM_DATA

key: 
    tuple(
        room number,
        room number,
    )

value:
    tuple(
        distance from room hallway spot to first spot in room (index 0 of the room),
        [
            hallway spot that must be open,
            another hallway spot that must be open,
            ...
        ],
    )
"""
ROOM_TO_ROOM_DATA = {
    (0, 1): (4, [2]),
    (0, 2): (6, [2, 3]),
    (0, 3): (8, [2, 3, 4]),
    (1, 0): (4, [2]),
    (1, 2): (4, [3]),
    (1, 3): (6, [3, 4]),
    (2, 0): (6, [2, 3]),
    (2, 1): (4, [3]),
    (2, 3): (4, [4]),
    (3, 0): (8, [2, 3, 4]),
    (3, 1): (6, [3, 4]),
    (3, 2): (4, [4]),
}


LEN_HALLWAY = 7

# --------------------------------------------------------
# |  0 |  1 |    |  2 |    |  3 |    |  4 |    |  5 |  6 |
# --------------------------------------------------------
#           |  7 |    | 11 |    | 15 |    | 19 |
#           ------    ------    ------    ------
#           |  8 |    | 12 |    | 16 |    | 20 |
#           ------    ------    ------    ------
#           |  9 |    | 13 |    | 17 |    | 21 |
#           ------    ------    ------    ------
#           | 10 |    | 14 |    | 18 |    | 22 |
#           ------    ------    ------    ------
#     ROOM:    0         1         2         3


letter_to_state = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
}
state_to_letter = {v: k for k, v in letter_to_state.items()}


def parse_input(lines: list[str], insert: str = None):
    room_rows = [line[3:10:2] for line in lines[2:4]]
    if insert:
        to_insert = [line.strip()[1::2] for line in insert.strip().splitlines()]
        room_rows = room_rows[:1] + to_insert + room_rows[1:]
    rooms = []
    for this in zip(*room_rows):
        rooms.append(tuple(letter_to_state[i] for i in this))
    return tuple(rooms)


def enter_room_if_possible(state, room_depth) -> tuple[int, list[int]]:
    for i, to_move in enumerate(state[:LEN_HALLWAY]):
        if to_move:
            distance, to_check = PATH_DATA[(i, to_move - 1)]
            if not any(state[j] for j in to_check):
                room_start_index = LEN_HALLWAY + (to_move - 1) * room_depth
                room_end_index = LEN_HALLWAY + (to_move) * room_depth
                room = state[room_start_index:room_end_index]
                if all(j in (0, to_move) for j in room):
                    spot = room.count(0) - 1
                    cost = (distance + spot) * 10 ** (to_move - 1)
                    next_state = move(state, i, 0, room_start_index + spot, to_move)
                    return cost, next_state
    for i in range(4):
        room_start_index = LEN_HALLWAY + i * room_depth
        room_end_index = LEN_HALLWAY + (i + 1) * room_depth
        room = state[room_start_index:room_end_index]
        if all(j in (0, i + 1) for j in room):
            continue
        spot = room.count(0)
        to_move = room[spot]
        if to_move == i + 1:
            continue
        distance, to_check = ROOM_TO_ROOM_DATA[(i, to_move - 1)]
        if not any(state[j] for j in to_check):
            dest_room_start_index = LEN_HALLWAY + (to_move - 1) * room_depth
            dest_room_end_index = LEN_HALLWAY + (to_move) * room_depth
            dest_room = state[dest_room_start_index:dest_room_end_index]
            if all(j in (0, to_move) for j in dest_room):
                dest_spot = dest_room.count(0) - 1
                cost = (spot + distance + dest_spot) * 10 ** (to_move - 1)
                next_state = move(
                    state,
                    room_start_index + spot,
                    0,
                    dest_room_start_index + dest_spot,
                    to_move,
                )
                return cost, next_state
    return 0, state


def move(state, index1, value1, index2, value2):
    new_state = list(state)
    new_state[index1] = value1
    new_state[index2] = value2
    return new_state


def all_moves_to_hallway(state, room_depth):
    to_return = []
    for i in range(4):
        room_start_index = LEN_HALLWAY + i * room_depth
        room_end_index = LEN_HALLWAY + (i + 1) * room_depth
        room = state[room_start_index:room_end_index]
        if all(token in (0, i + 1) for token in room):
            continue
        spot = room.count(0)
        to_move = room[spot]
        for j, token in enumerate(state[:LEN_HALLWAY]):
            if not token:
                distance, to_check = PATH_DATA[(j, i)]
                if not any(state[k] for k in to_check):
                    cost = (distance + spot) * 10 ** (to_move - 1)
                    next_state = move(state, j, to_move, room_start_index + spot, 0)
                    to_return.append((cost, next_state))
    return to_return


def all_valid_moves(state, room_depth):
    cost, state = enter_room_if_possible(state, room_depth)
    if cost > 0:
        return [(cost, state)]
    return all_moves_to_hallway(state, room_depth)


def done(state, room_depth):
    rooms = state[LEN_HALLWAY:]
    solved = [1] * room_depth + [2] * room_depth + [3] * room_depth + [4] * room_depth
    return rooms == solved


def to_diagram(state, room_depth):
    diagram = ["#" * 13]
    hallway = f"".join(state_to_letter.get(i, ".") for i in state[:LEN_HALLWAY])
    diagram.append(
        f"#{hallway[:2]}.{hallway[2]}.{hallway[3]}.{hallway[4]}.{hallway[5:]}#"
    )
    for i in range(room_depth):
        row = state[(LEN_HALLWAY + i) :: room_depth]
        home_row = "#".join(state_to_letter.get(i, ".") for i in row)
        if i == 0:
            diagram.append(f"###{home_row}###")
        else:
            diagram.append(f"  #{home_row}#")
    diagram.append("  " + "#" * 9)
    return "\n".join(diagram)


def calculate_energy_to_solve(lines: list[str], insert: str = None) -> int:
    rooms = parse_input(lines, insert)
    room_depth = len(rooms[0])
    start = [0, 0, 0, 0, 0, 0, 0] + [val for sublist in rooms for val in sublist]
    start_tuple = tuple(start)
    came_from = {start_tuple: start_tuple}
    cost_so_far = {start_tuple: 0}
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        next_item = heapq.heappop(queue)
        current = next_item[1]
        current_tuple = tuple(current)
        if done(current, room_depth):
            break
        for cost, next_state in all_valid_moves(current, room_depth):
            next_state_tuple = tuple(next_state)
            new_cost = cost_so_far[current_tuple] + cost
            if (
                next_state_tuple not in cost_so_far
                or new_cost < cost_so_far[next_state_tuple]
            ):
                cost_so_far[next_state_tuple] = new_cost
                came_from[next_state_tuple] = current
                heapq.heappush(queue, (new_cost, next_state))
    return cost_so_far[current_tuple]


def part1(lines: list[str]):
    return calculate_energy_to_solve(lines)


def part2(lines: list[str]):
    insert = """
      #D#C#B#A#
      #D#B#A#C#
    """
    return calculate_energy_to_solve(lines, insert)
