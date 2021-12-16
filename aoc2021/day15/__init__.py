import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra_path_length


def build_map(lines: list[str], extended: bool = False) -> dict[(int, int), int]:
    risk_map = {}
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            risk_map[(i, j)] = int(val)
    if extended:
        extended_map = {}
        ni = len(lines)
        nj = len(lines[0])
        for di in range(5):
            for dj in range(5):
                for (i, j), val in risk_map.items():
                    new_point = (i + di * ni, j + dj * nj)
                    new_val = (val + di + dj - 1) % 9 + 1
                    extended_map[new_point] = new_val
        risk_map = extended_map
    return risk_map


def build_graph(risk_map: dict[(int, int), int]) -> nx.Graph:
    G = nx.DiGraph()
    for i, j in risk_map.keys():
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (i + di, j + dj)
            if neighbor in risk_map:
                G.add_edge((i, j), neighbor, weight=risk_map[neighbor])
    return G


def shortest_path_length(G: nx.Graph) -> int:
    start = (min(i for i, j in G), min(j for i, j in G))
    end = (max(i for i, j in G), max(j for i, j in G))
    return dijkstra_path_length(G, start, end)


def part1(lines: list[str]) -> int:
    risk_map = build_map(lines)
    G = build_graph(risk_map)
    return shortest_path_length(G)


def part2(lines: list[str]):
    risk_map = build_map(lines, True)
    G = build_graph(risk_map)
    return shortest_path_length(G)
