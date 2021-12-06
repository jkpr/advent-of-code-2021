# Advent of Code 2021

These are my solutions to Advent of Code 2021. The solutions are in the `__init__.py` files for each day's package. Sometimes, there is an solution in `alternate.py` (or in an `alternate` subpackage if the code needs to broken across modules. The main solution code is still in `alternate/__init__.py`).

Try the problems yourself at [https://adventofcode.com/2021/](https://adventofcode.com/2021/).

Feel free to create a Github issue if you want to discuss anything!

# Usage

1. Clone this repo: `git clone https://github.com/jkpr/advent-of-code-2021`
2. Change into the new directory: `cd advent-of-code-2021`
3. Run `make env` to build the environment.
4. Activate the environment with `source env/bin/activate`
5. Run a CLI for day `N`'s code with `python3 -m aoc2021 -d N`, e.g. `python3 -m aoc2021 -d 1`.

The CLI is common for each day. The main patterns for options are:

- `-t` to run part 1 with `test_input.txt`
- `-2` to run part 2
- `-t -2` to run part 2 with `test_input.txt`
- `-t 1` to run part 1 with `test_input1.txt`
- `-t 1 -2` to run part 2  with `test_input1.txt`

# Table of contents

| `Day % 5 == 0` | `Day % 5 == 1` | `Day % 5 == 2` | `Day % 5 == 3` | `Day % 5 == 4` |
| --- | --- | --- | --- | --- |
| | 1 · [_notes_](#day-1) · [_code_](aoc2021/day01) | 2 · [_notes_](#day-2) · [_code_](aoc2021/day02) | 3 · [_notes_](#day-3) · [_code_](aoc2021/day03) | 4 · [_notes_](#day-4) · [_code_](aoc2021/day04) |
| 5 · [_notes_](#day-5) · [_code_](aoc2021/day05) | 6 · [_notes_](#day-6) · [_code_](aoc2021/day06) | 7 · [_notes_](#day-7) · [_code_](aoc2021/day07) | 8 · [_notes_](#day-8) · [_code_](aoc2021/day08) | 9 · [_notes_](#day-9) · [_code_](aoc2021/day09) |
| 10 · [_notes_](#day-10) · [_code_](aoc2021/day10) | 11 · [_notes_](#day-11) · [_code_](aoc2021/day11) | 12 · [_notes_](#day-12) · [_code_](aoc2021/day12) | 13 · [_notes_](#day-13) · [_code_](aoc2021/day13) | 14 · [_notes_](#day-14) · [_code_](aoc2021/day14) |
| 15 · [_notes_](#day-15) · [_code_](aoc2021/day15) | 16 · [_notes_](#day-16) · [_code_](aoc2021/day16) | 17 · [_notes_](#day-17) · [_code_](aoc2021/day17) | 18 · [_notes_](#day-18) · [_code_](aoc2021/day18) | 19 · [_notes_](#day-19) · [_code_](aoc2021/day19) |
| 20 · [_notes_](#day-20) · [_code_](aoc2021/day20) | 21 · [_notes_](#day-21) · [_code_](aoc2021/day21) | 22 · [_notes_](#day-22) · [_code_](aoc2021/day22) | 23 · [_notes_](#day-23) · [_code_](aoc2021/day23) | 24 · [_notes_](#day-24) · [_code_](aoc2021/day24) |
| 25 · [_notes_](#day-25) · [_code_](aoc2021/day25) | | | | |

# Day 1

The best way I know to iterate a window through a list is to `zip(my_list, my_list[1:])`. Iterating through sums of triples is the same as iterating through `zip(my_list, my_list[1:], my_list[2:], my_list[3:])` and comparing the first three to the last three.

# Day 2

Keeping track of state while looping through the lines of the input. Fairly straightforward.

# Day 3

Interesting problem. For my input, part 2 filters down to a single number for both oxygen and CO2. Therefore, we don't need to keep track of the bits as we go, just take the single number as the result. To take a string and convert it to a number:

```python
num_as_str = "101010111"
num_as_int = int(num_as_str, base=2)
```

# Day 4

Sometimes we have to break input up based on a blank line (here the game boards are separated by a blank line). This is how I have done that with `lines` that is a list of lines:

```python
result = []
chunks = "\n".join(lines).split("\n\n")
for chunk in chunks:
    result.append(chunk.split("\n"))
```

I could have modeled this exactly as the problem described, with Board objects and crossed off numbers. However, I went a more "functional" route, and built up two datastructures:

- all possible bingos per board, stored as sets
- each board as a set of numbers

For each new number, I made a set of called numbers:

```python
called = set(numbers[:i])
```

I made a set and compared that against all possible bingos. 

```python
for board_bingos in all_board_bingos:
    for bingo in board_bingos:
        if called & bingo == bingo:
            ...  # Winner!
```

When there was a match, I started with that board's set of numbers and took away the called set of numbers:

```python
left_over = board_numbers - called
```

Then performed the calculation with `left_over` and `numbers[:i]` to get the final score.

# Day 5

Knowing how to parse input helped get a quick result. Using [`re.findall`][5a] can get all numbers found in a line. Specifically, `re.findall(r"\d+", line)` returns a list of all integers.

Finally, [`defaultdict`][5b] remains one the best ways to model a position. In this problem, we can add 1 to every position that every line crosses. The position should be a tuple for the coordinates.

```python
field = defaultdict(int)
for vent line in all vent lines:
    for each (x, y) position along a vent line:
        field[(x, y)] += 1
```

Then return the count of positions that have a value of 2 or more:

```python
sum(value >= 2 for value in field.values())
```

[5a]: https://docs.python.org/3/library/re.html#re.findall
[5b]: https://docs.python.org/3/library/collections.html#collections.defaultdict

# Day 6

This is exponential growth, and the key here is to not model each fish (you quickly run out of memory), but to model the lanternfish by internal clock.

So instead of

```
3,4,3,1,2
``

we have a dictionary of counts, keyed by the clock:

```
{3: 2, 4: 1, 1:1, 2:1}
```