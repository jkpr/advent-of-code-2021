from collections import deque

from .utils import already_has_extra_visit, get_edges


def bfs(
    start: str,
    end: str,
    edges: dict[str, list[str]],
    allow_extra: bool,
) -> list[tuple[str, ...]]:
    paths = []
    to_search = deque()
    to_search.append((start,))
    while to_search:
        path = to_search.popleft()
        if path[-1] == end:
            paths.append(path)
        else:
            for conn in edges[path[-1]]:
                if conn == start:
                    continue
                if conn.islower() and conn in path:
                    if not allow_extra:
                        continue
                    elif already_has_extra_visit(path):
                        continue
                to_search.append(path + (conn,))
    return paths


def part1(lines: list[str]):
    edges = get_edges(lines)
    result = bfs("start", "end", edges, False)
    return len(result)


def part2(lines: list[str]):
    edges = get_edges(lines)
    result = bfs("start", "end", edges, True)
    return len(result)
