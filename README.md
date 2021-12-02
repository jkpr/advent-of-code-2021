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

Nothing too special today...
