import importlib
from itertools import compress
import logging
from pathlib import Path
import time

import click

from aoc2021.utils import setup_logging


DEFAULT_TEST_FILE = "test_input.txt"
logger = logging.getLogger(__name__)


def get_input_file(folder: str, test_input: str | None) -> Path:
    root = Path(__file__).parent
    if test_input is None:
        file_name = "input.txt"
    elif test_input == DEFAULT_TEST_FILE:
        file_name = DEFAULT_TEST_FILE
    else:
        file_name = f"test_input{test_input}.txt"
    return root / folder / file_name


def read_lines(input_file: Path) -> list[str]:
    return input_file.read_text(encoding="utf-8").splitlines()


@click.command()
@click.option(
    "--day",
    "-d",
    required=True,
    type=click.IntRange(min=1, max=25),
    help="Which day's code to run.",
)
@click.option(
    "--part1",
    "-1",
    is_flag=True,
    help="Run part 1",
)
@click.option(
    "--part2",
    "-2",
    is_flag=True,
    help="Run part 2",
)
@click.option(
    "--test-input",
    "-t",
    is_flag=False,
    flag_value=DEFAULT_TEST_FILE,
    help=(
        "If not supplied, use real puzzle "
        'data from "input.txt". If given as a flag, use '
        f'"{DEFAULT_TEST_FILE}". If a value is given, it is '
        'treated as a suffix, as in "test_input[SUFFIX].txt".'
    ),
)
@click.option(
    "--alternate",
    "-a",
    is_flag=True,
    help="Run the alternate solution, if it exists.",
)
@click.option(
    "--silent",
    "-s",
    is_flag=True,
    help="Do not show logs.",
)
def cli(
    day: int,
    part1: bool,
    part2: bool,
    test_input: str,
    alternate: bool,
    silent: bool,
):
    if not silent:
        setup_logging()
    name = f"..day{str(day).zfill(2)}"
    input_file = get_input_file(name[2:], test_input)
    if alternate:
        name = f"{name}.alternate"
    module = importlib.import_module(name, package=__name__)
    lines = read_lines(input_file)
    logger.info(f"Puzzle input: {input_file!s}")
    start = time.perf_counter()
    parts = ", ".join(
        compress(["part 1", "part 2"], [part1 or not part2, part2 or not part1])
    )
    logger.info("Running %s", parts)
    if part1 or not part2:
        result1 = module.part1(lines)
        print("Returned result for part 1:", result1)
    if part2 or not part1:
        result2 = module.part2(lines)
        print("Returned result for part 2:", result2)
    end = time.perf_counter()
    logger.info(f"Time elapsed: {end-start:.4f} seconds")
