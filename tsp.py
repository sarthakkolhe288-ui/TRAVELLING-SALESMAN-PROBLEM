"""Interactive Traveling Salesman Problem Demonstration."""
from algorithms.brute_force import solve as brute_force
from algorithms.dynamic_programming import solve as held_karp
from algorithms.nearest_neighbor import solve as nearest_neighbor
from utils.helpers import generate_random_matrix, timed_call, validate_matrix

def city_name(i):
    return chr(ord("A") + i)

def format_route(route):
    return " -> ".join(city_name(i) for i in route)

def print_matrix(matrix):
    print("\nDistance Matrix")
    print("     " + " ".join(f"{city_name(i):>5}" for i in range(len(matrix))))
    for i, row in enumerate(matrix):
        print(f"{city_name(i):>3} " + " ".join(f"{v:>5}" for v in row))

def compare_algorithms(matrix):
    algorithms = [("Brute Force", brute_force), ("Dynamic Programming", held_karp), ("Nearest Neighbor", nearest_neighbor)]
    results = []
    for name, func in algorithms:
        (cost, route), elapsed = timed_call(func, matrix)
        results.append((name, cost, route, elapsed))
    return results

def print_results(results):
    print("\n" + "=" * 72)
    print("ALGORITHM RESULTS")
    print("=" * 72)
    print(f"{'Algorithm':<24}{'Distance':>14}{'Time (sec)':>16}")
    print("-" * 72)
    for name, cost, route, elapsed in results:
        print(f"{name:<24}{cost:>14.2f}{elapsed:>16.8f}")
        print(f"  Route: {format_route(route)}")
    exact = next(r for r in results if r[0] == "Dynamic Programming")
    print(f"\nExact optimal distance: {exact[1]:.2f}")
    nn = next(r for r in results if r[0] == "Nearest Neighbor")
    gap = ((nn[1] - exact[1]) / exact[1] * 100) if exact[1] else 0
    print(f"Nearest Neighbor gap from optimum: {gap:.2f}%")

def get_matrix():
    choice = input("Generate random matrix? (y/n): ").strip().lower()
    if choice == "y":
        n = int(input("Number of cities (2-10 recommended): "))
        return generate_random_matrix(n, seed=42)
    n = int(input("Number of cities: "))
    print("Enter each row with", n, "space-separated distances.")
    matrix = [list(map(float, input("> ").split())) for _ in range(n)]
    validate_matrix(matrix)
    return matrix

def main():
    print("=" * 72)
    print("          TRAVELING SALESMAN PROBLEM DEMONSTRATION")
    print("=" * 72)
    matrix = None
    while True:
        print("\n1. Enter / Generate Distance Matrix")
        print("2. Solve using Brute Force")
        print("3. Solve using Dynamic Programming (Held-Karp)")
        print("4. Solve using Nearest Neighbor")
        print("5. Compare Algorithms")
        print("6. Exit")
        choice = input("\nEnter choice: ").strip()
        if choice == "6":
            print("Thank you for using the TSP Demonstration.")
            break
        if choice == "1":
            matrix = get_matrix()
            print_matrix(matrix)
            continue
        if choice not in {"2", "3", "4", "5"}:
            print("Invalid choice.")
            continue
        if matrix is None:
            matrix = get_matrix()
        print_matrix(matrix)
        if choice == "2":
            func, label = brute_force, "Brute Force"
        elif choice == "3":
            func, label = held_karp, "Dynamic Programming"
        elif choice == "4":
            func, label = nearest_neighbor, "Nearest Neighbor"
        else:
            print_results(compare_algorithms(matrix))
            continue
        (cost, route), elapsed = timed_call(func, matrix)
        print(f"\n{label} Route : {format_route(route)}")
        print(f"Tour Cost         : {cost:.2f}")
        print(f"Execution Time    : {elapsed:.8f} sec")

if __name__ == "__main__":
    main()
