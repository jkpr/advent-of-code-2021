from collections import defaultdict


def get_counts(counter: dict[str, int], first: str, last: str) -> dict[str, str]:
    counts = defaultdict(int)
    for k, v in counter.items():
        counts[k[0]] += v
        counts[k[1]] += v
    counts[first] += 1
    counts[last] += 1
    return {k: v // 2 for k, v in counts.items()}
