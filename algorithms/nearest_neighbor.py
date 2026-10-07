"""Greedy TSP approximation using Nearest Neighbor."""
def solve(distance, start=0):
    n = len(distance)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [start, start]
    unvisited = set(range(n))
    unvisited.remove(start)
    route, total, current = [start], 0, start
    while unvisited:
        nxt = min(unvisited, key=lambda city: distance[current][city])
        total += distance[current][nxt]
        route.append(nxt)
        current = nxt
        unvisited.remove(nxt)
    total += distance[current][start]
    route.append(start)
    return total, route
