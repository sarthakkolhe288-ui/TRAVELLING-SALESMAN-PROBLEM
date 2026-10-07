"""Input validation, random matrices and timing helpers."""
import random
import time

def validate_matrix(matrix):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Distance matrix must be non-empty and square.")
    if any(value < 0 for row in matrix for value in row):
        raise ValueError("Distances cannot be negative.")
    if any(matrix[i][i] != 0 for i in range(len(matrix))):
        raise ValueError("Diagonal entries must be zero.")
    return True

def generate_random_matrix(n, low=10, high=100, seed=None):
    rng = random.Random(seed)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = matrix[j][i] = rng.randint(low, high)
    return matrix

def timed_call(function, *args, **kwargs):
    start = time.perf_counter()
    result = function(*args, **kwargs)
    return result, time.perf_counter() - start
