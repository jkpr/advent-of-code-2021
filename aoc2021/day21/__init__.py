from collections import namedtuple
from functools import cache, reduce
from itertools import product


GameState = namedtuple("GameState", "p1,p2,p1_score,p2_score,turn,die,rolls")


def turn(state) -> GameState:
    rolls = [state.die % 100 + 1, (state.die + 1) % 100 + 1, (state.die + 2) % 100 + 1]
    move = sum(rolls)
    mover = (state[state.turn] - 1 + move) % 10 + 1
    next_squares = [state.p1, state.p2]
    next_squares[state.turn] = mover
    next_scores = [state.p1_score, state.p2_score]
    next_scores[state.turn] += mover
    return GameState(
        *next_squares,
        *next_scores,
        (state.turn + 1) % 2,
        (state.die + 2) % 100 + 1,
        state.rolls + 3,
    )


def part1(lines: list[str]):
    p1 = int(lines[0].rsplit(maxsplit=1)[1])
    p2 = int(lines[1].rsplit(maxsplit=1)[1])
    state = GameState(p1, p2, 0, 0, 0, 0, 0)
    while state.p1_score < 1000 and state.p2_score < 1000:
        state = turn(state)
    return min(state.p1_score, state.p2_score) * state.rolls


DiracState = namedtuple("DiracState", "p1,p2,p1_score,p2_score,turn")


@cache
def win_counts(state: DiracState) -> tuple[int, int]:
    if state.p1_score >= 21:
        return (1, 0)
    elif state.p2_score >= 21:
        return (0, 1)
    next_win_counts = []
    for rolls in product([1, 2, 3], repeat=3):
        move = sum(rolls)
        mover = (state[state.turn] - 1 + move) % 10 + 1
        next_squares = [state.p1, state.p2]
        next_squares[state.turn] = mover
        next_scores = [state.p1_score, state.p2_score]
        next_scores[state.turn] += mover
        next_state = DiracState(
            *next_squares,
            *next_scores,
            (state.turn + 1) % 2,
        )
        next_win_counts.append(win_counts(next_state))
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), next_win_counts, (0, 0))


def part2(lines: list[str]):
    p1 = int(lines[0].rsplit(maxsplit=1)[1])
    p2 = int(lines[1].rsplit(maxsplit=1)[1])
    state = DiracState(p1, p2, 0, 0, 0)
    return max(win_counts(state))
