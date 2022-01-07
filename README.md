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
chunks = "\n".join(lines).split("\n\n")
result = [chunk.strip().splitlines() for chunk in chunks]
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
```

we have a dictionary of counts, keyed by the clock:

```
{3: 2, 4: 1, 1:1, 2:1}
```

# Day 7

The sum of numbers `1..N` is `N * (N+1) / 2`. This formula was used to find the ideal horizontal position.

# Day 8

A set can be hashable if it is a [`frozenset`][8a]! Therefore it can be a key in a dictionary.

[8a]: https://docs.python.org/3/library/stdtypes.html#frozenset

# Day 9

A fun area search with recursion. In order to get the most common, I used [`collections.Counter.most_common()`][9a] which returns a list of tuples (the value and the count of the value).

[9a]: https://docs.python.org/3/library/collections.html#collections.Counter.most_common

# Day 10

Tried to be more expressive rather than concise. Fairly straightforward LIFO stack stuff.

# Day 11

Probably the only interesting thing is how I iterated through neighbors:

```python
def neighbors(i: int, j: int, dim: int) -> tuple[int, int]:
    for d in product([-1, 0, 1], repeat=2):
        if d != (0, 0):
            if (new_i := i + d[0]) in range(dim) and (new_j := j + d[1]) in range(dim):
                yield new_i, new_j
```

# Day 12

The `__init__.py` solution has a breadth-first search (BFS). The `alternate.py` has a recursive depth-first search (DFS) solution.

A BFS typically has a deque, popping the next one to examine from the left side, and adding new ones to search to the right side. The search algorithm runs until there are no more items in the deque. For my first pass, I used a standard list (which must resize / reorder as things are added and removed from the first index). When I switched to [`collections.deque`][12a], the execution time decreased by 50%.

[12a]: https://docs.python.org/3/library/collections.html#collections.deque

# Day 13

I used the trick for splitting into chunks from [Day 4](#day-4).

Today I used [`dataclass`][13a] with `frozen=True` to represent a point. This is so that the dataclass can be a member of a set.

Another useful feature of dataclasses is [`replace`][13b] which makes a new object of the same class, but with replaced properties. For example:

```python
replace(point, **{'x': new_x})
```

[13a]: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
[13b]: https://docs.python.org/3/library/dataclasses.html#dataclasses.replace

# Day 14

The main solution at `__init__.py` goes from one polymer to the next generation polymer. An interesting recursive solution, using caching, is at `alternate.py`.

In both, I keep track of counts of bigrams (two consecutive letters).

The [`functools.cache`][14a] is handy because it can short-circuit calculating results. This is useful, and it helps often, in recursion because the code often visits the same areas of the search space multiple times.

```python
from collections import Counter
import functools


@functools.cache
def next_gen_recursive(bigram: str, times: int) -> Counter:
    if times == 0:
        return Counter([bigram])
    middle = rules[bigram]
    left = next_gen_recursive(f"{bigram[0]}{middle}", times - 1)
    right = next_gen_recursive(f"{middle}{bigram[1]}", times - 1)
    return left + right
```

Take note that `functools.cache` is new as of Python 3.9. It is equivalent to `functools.lru_cache(maxsize=None)`.

Without caching, each bigram results in two calls to the recursive function. For part two, this would have been repeated 40 times, so there would have been `2^40 = 1,099,511,627,776` calls to the recursive function for each bigram in the starting polymer.

With caching on the other hand, with my input data, the cache info is `CacheInfo(hits=3140, misses=3291, maxsize=None, currsize=3291)`. So the function gets called only `3140 + 3291 = 6431` times.

[14a]: https://docs.python.org/3/library/functools.html#functools.cache

# Day 15

Python has a beautiful package called [`networkx`][15a] and it saves the day today. It can build a graph and it has algorithms for finding shortest path length from different nodes. It has Dijkstra's shortest path algorithm, separate methods to get the path and also the path length.

In terms of modeling, consider a smaller example

```
19
24
```

This becomes a directed graph, where for each node, A -> B, the weight of the edge is the value at B. Something like this:

```
         9
        --->
  (0,0) <--- (0,1)
  |  ^    1   | ^
 2|  |        | |
  |  |1      4| | 9
  |  |        | |
  v  |   4    v |
  (1,0) ---> (1,1)
        <---
          2
```

This information is saved in the graph.

[15a]: https://networkx.org/documentation/stable/index.html

# Day 16

There were a lot of fun things today. First, I got to use Python 3.10's flagship feature, the [match-case construct][16a], a.k.a. structural pattern matching. In this case, it wasn't too fancy, just a match-case on the packet type, so just matching literal values. From what I have read, it is a well-thought out feature.

Another interesting feature is postponed evaluation of annotations, [PEP 563][16b]. This allows us to write:

```python
from __future__ import annotations


class A:

    @classmethod
    def build(cls) -> A:
        ...
```

instead of

```python
class A:

    @classmethod
    def build(cls) -> "A":
        ...
```

Hopefully someday in the future, this will be the default and the `from __future__ import annotations` will no longer be needed.

Finally, I used data classes to parse out the ticker tape of packets. There are `Packet`, `Header`, and `Literal` classes.
Each class has a `from_tape` method that parses out an instance of that class from the ticker tape starting at index `i`.
For example,

```python
class Header:
    ...
    @classmethod
    def from_tape(cls, tape: str, i: int) -> Header:
        ...
```

This leads to some simple solutions for part 1 and part 2.


[16a]: https://www.python.org/dev/peps/pep-0636/
[16b]: https://www.python.org/dev/peps/pep-0563/

# Day 17

Probably for the first time ever, I use [`itertools.count()`][17a]. I think it is easier to do:

```python
for n in itertools.count():
    ...
```

than

```python
n = 0
while True:
    ...
    n += 1
```

[17a]: https://docs.python.org/3/library/itertools.html#itertools.count

# Day 18

I use regex to look for numbers before and after pairs that are nested more than 4 deep. I use the `start` and `end` properties of [`re.Match`][18a] to get the indices where the match starts and stops.

I use [`itertools.accumulate()`][18b] to add the input snail numbers consecutively. That is definitely the right tool for the job.

In order to get the magnitude, I [`eval`][18c] the final string to turn it into nested lists with ints.

Finally, [`itertools.combinations`][18d] is perfect for looking at all sets of two snail numbers in order to get the maximum magnitude.

[18a]: https://docs.python.org/3/library/re.html#match-objects
[18b]: https://docs.python.org/3/library/itertools.html#itertools.accumulate
[18c]: https://docs.python.org/3/library/functions.html#eval
[18d]: https://docs.python.org/3/library/itertools.html#itertools.combinations

# Day 19

This is the hardest challenge of Advent of Code 2021.

Interesting Python things:

I made a type alias for typing annotations:

```python
Point = tuple[int, int, int]
```

`Point` is much easier / shorter than `tuple[int, int, int]`. See [typing documentation for aliases][19a].

Used `itertools.combinations()` to look at every combination of two scanners.

[19a]: https://docs.python.org/3/library/typing.html#type-aliases

# Day 20

Did a fairly interesting thing to get the enhancement algorithm index:

```python
...
index_bits = (
    int((i + di, j + dj) in image)
    if min_i <= i + di <= max_i and min_j <= j + dj <= max_j
    else default
    for di, dj in product([1, 0, -1], repeat=2)
)
index = sum(1 << n if bit else 0 for n, bit in enumerate(index_bits))
```

Using [`itertools.product()`][20a] this way gets the pixels in the right order (least significant to most significant). Of course `1 << n` could be `2 ** n`.

[20a]: https://docs.python.org/3/library/itertools.html#itertools.product

# Day 21

Used a [namedtuple][21a] to represent the game state.

Got to use a [functools.cache][21b] for part 2 since the number of game paths is too large to simulate individually.
By the way, my cache info is:

```
CacheInfo(hits=765674, misses=43220, maxsize=None, currsize=43220)
```

This code runs in about 1.2 seconds.

I also get to use [`functools.reduce()`][21c] for the first time. This is to add up all the win tallies (tuples) from the next 27 Dirac game states.

[21a]: https://docs.python.org/3/library/collections.html#collections.namedtuple
[21b]: https://docs.python.org/3/library/functools.html#functools.cache
[21c]: https://docs.python.org/3/library/functools.html#functools.reduce

# Day 22

I define a `Cube` class that supports intersection and subtraction with other cubes.

- Intersection returns another `Cube`.
- Subtraction returns a list of from 0 up to 6 other cuboids. 
  - Subtraction returns a list of 0—an empty list—cuboids if the subtracted amount completely covers the original cuboid. 
  - Otherwise, I divide up the remaining volume up into cuboids using the planes of the intersection cube faces as dividing lines.

I use the builtin [`slice()`][22a] to pass to a list object and be flexible with how many items I am taking.

- `my_list[slice(0, 20)]` takes the first 20 items.
- `my_list[slice(0, None)]` takes all items in the list.

[22a]: https://docs.python.org/3/library/functions.html#slice

# Day 23

Today we implement Dijkstra's shortest path algorithm.
In order to do that, we need a priority queue so that the next thing we pop off to search has the shortest edge weight (energy) of everything we know about.
This is where Python's [`heapq`][23a] comes in. It works on a run-of-the-mill list.

For example:

```python
import heapq


queue = []
start = get_start_configuration()
heapq.heappush(queue, (0, start))
while queue:
    next_item = heapq.heappop(queue)
    ...
```

[23a]: https://docs.python.org/3/library/heapq.html

# Day 24

Not too much interesting in terms of Python. This is a challenge in deciphering what the instructions are doing.

We need to iterate over the input (`lines`) in chunks of 18. That can be done like this:

```python
chunk_size = 18
for i in range(len(lines) // chunk_size):
    instructions = lines[slice(i * chunk_size, (i + 1) * chunk_size)]
```

This does not get a partial chunk at the end if there is one.

# Day 25

- Build up a grid with a `dict()` and keep the dimensions:

```python
sea_floor = {}
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        sea_floor[(i, j)] = ch
dim = i + 1, j + 1
```

- Count the generations with [`itertools.count()`][25a]
- When some condition is met, then return `i`.
- Advance one generation to the next by some puzzle-specific rules.

```python
for i in itertools.count():
    if done(next_sea_floor):
        return i
    next_sea_floor = get_next(sea_floor)
```

[25a]: https://docs.python.org/3/library/itertools.html#itertools.count