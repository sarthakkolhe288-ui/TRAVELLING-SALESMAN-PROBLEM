"""Exact TSP using Held-Karp subset dynamic programming."""
from itertools import combinations

def solve(distance):
    n = len(distance)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0, 0]

    dp, parent = {}, {}
    for last in range(1, n):
        mask = 1 << (last - 1)
        dp[(mask, last)] = distance[0][last]
        parent[(mask, last)] = 0

    for size in range(2, n):
        for subset in combinations(range(1, n), size):
            mask = sum(1 << (v - 1) for v in subset)
            for last in subset:
                prev_mask = mask ^ (1 << (last - 1))
                best, best_prev = float("inf"), None
                for prev in subset:
                    if prev == last:
                        continue
                    candidate = dp[(prev_mask, prev)] + distance[prev][last]
                    if candidate < best:
                        best, best_prev = candidate, prev
                dp[(mask, last)] = best
                parent[(mask, last)] = best_prev

    full_mask = (1 << (n - 1)) - 1
    best_cost, last_city = float("inf"), None
    for last in range(1, n):
        candidate = dp[(full_mask, last)] + distance[last][0]
        if candidate < best_cost:
            best_cost, last_city = candidate, last

    route = [0] * (n + 1)
    route[-1] = 0
    mask, last = full_mask, last_city
    for pos in range(n - 1, 0, -1):
        route[pos] = last
        prev = parent[(mask, last)]
        mask ^= 1 << (last - 1)
        last = prev
    return best_cost, route
