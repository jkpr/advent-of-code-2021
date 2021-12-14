from .utils import already_has_extra_visit, get_edges


def dfs(
    start: str,
    end: str,
    path: tuple[str, ...],
    edges: dict[str, list[str]],
    allow_extra: bool,
) -> list[tuple[str, ...]]:
    curr = path[-1]
    if curr == end:
        return [path]
    sub_paths = []
    for conn in edges[curr]:
        if conn == start:
            continue
        if conn.islower() and conn in path:
            if not allow_extra:
                continue
            elif already_has_extra_visit(path):
                continue
        results = dfs(start, end, path + (conn,), edges, allow_extra)
        sub_paths.extend(results)
    return sub_paths


def part1(lines: list[str]):
    edges = get_edges(lines)
    result = dfs("start", "end", ("start",), edges, allow_extra=False)
    return len(result)


def part2(lines: list[str]):
    edges = get_edges(lines)
    result = dfs("start", "end", ("start",), edges, allow_extra=True)
    return len(result)
