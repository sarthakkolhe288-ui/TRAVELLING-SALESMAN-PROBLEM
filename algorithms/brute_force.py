"""Exact TSP using exhaustive permutation search."""
from itertools import permutations

def solve(distance):
    n = len(distance)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0, 0]
    best_cost = float("inf")
    best_route = None
    for perm in permutations(range(1, n)):
        route = (0,) + perm + (0,)
        cost = sum(distance[route[i]][route[i+1]] for i in range(n))
        if cost < best_cost:
            best_cost, best_route = cost, list(route)
    return best_cost, best_route
