import logging


def setup_logging():
    logger = logging.getLogger("aoc2021")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.NOTSET)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def lines_to_int(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]
