# Traveling Salesman Problem Demonstration

## Project Description
A DAA mini-project demonstrating the Traveling Salesman Problem using three algorithm-design techniques: exhaustive search, Dynamic Programming (Held–Karp), and the Nearest Neighbor greedy heuristic.

## Objectives
- Model TSP as a weighted graph.
- Implement exact and approximate algorithms.
- Demonstrate optimization through Dynamic Programming.
- Verify correctness using automated tests.
- Compare theoretical and practical performance.

## Algorithms
### 1. Brute Force
Enumerates every permutation of the cities after fixing the start city.
- Time: **O((n-1)!)**
- Auxiliary space: **O(n)**
- Optimal: **Yes**

### 2. Held–Karp Dynamic Programming
Uses `dp[mask][i]` to store the minimum cost of visiting a subset and ending at city `i`.
- Time: **O(n² × 2ⁿ)**
- Space: **O(n × 2ⁿ)**
- Optimal: **Yes**

### 3. Nearest Neighbor
Repeatedly chooses the closest unvisited city.
- Time: **O(n²)**
- Space: **O(n)**
- Optimal: **No guarantee**

## Correctness
Brute Force checks all possible tours, so its minimum is globally optimal. Held–Karp uses optimal substructure and considers every possible predecessor in each DP state, so the final minimum is also globally optimal. Nearest Neighbor correctly implements its greedy rule and returns a valid closed tour, but local choices do not guarantee a global optimum.

## Complexity Comparison

| Algorithm | Time | Space | Optimal |
|---|---:|---:|---|
| Brute Force | O((n-1)!) | O(n) auxiliary | Yes |
| Held–Karp DP | O(n² 2ⁿ) | O(n 2ⁿ) | Yes |
| Nearest Neighbor | O(n²) | O(n) | No |

## Technologies
- Python 3.10+
- Python standard library
- `unittest`
- `time.perf_counter()`
- No external packages required

## Execution

```bash
python tsp.py
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Sample Input

```text
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

## Sample Output
See `docs/sample_output.txt`.

For the sample matrix, the exact optimal tour cost is **80**.

## Repository Structure

```text
Traveling-Salesman-Problem-Demonstration/
├── README.md
├── tsp.py
├── requirements.txt
├── algorithms/
│   ├── brute_force.py
│   ├── dynamic_programming.py
│   └── nearest_neighbor.py
├── utils/
│   └── helpers.py
├── tests/
│   └── test_tsp.py
├── screenshots/
└── docs/
    ├── sample_output.txt
    └── Project_Report.pdf
```

## GitHub Upload

```bash
git init
git add .
git commit -m "Add TSP DAA mini project"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## Conclusion
The project shows the trade-off between exactness and computational cost. Brute Force is simple but factorial, Held–Karp is an optimized exact approach with exponential complexity, and Nearest Neighbor is polynomial-time but heuristic.

## Future Scope
- Branch and Bound
- 2-opt improvement
- Graphical route visualization
- Benchmark graphs
- Asymmetric TSP
- Real map data
