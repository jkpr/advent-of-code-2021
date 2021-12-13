from collections import Counter, defaultdict


def already_has_extra_visit(path: tuple[str, ...]) -> bool:
    visit_counts = Counter(cave for cave in path if cave.islower()).values()
    return any(count > 1 for count in visit_counts)


def get_edges(lines: list[str]) -> dict[str, set[str]]:
    edges = defaultdict(list)
    for line in lines:
        a, b = line.split("-")
        edges[a].append(b)
        edges[b].append(a)
    return edges
