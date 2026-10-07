import unittest
from algorithms.brute_force import solve as brute_force
from algorithms.dynamic_programming import solve as held_karp
from algorithms.nearest_neighbor import solve as nearest_neighbor

class TestTSP(unittest.TestCase):
    def setUp(self):
        self.matrix = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]

    def test_exact_algorithms_agree(self):
        self.assertEqual(brute_force(self.matrix)[0], 80)
        self.assertEqual(held_karp(self.matrix)[0], 80)

    def test_nearest_neighbor_route(self):
        cost, route = nearest_neighbor(self.matrix)
        self.assertEqual(cost, 80)
        self.assertEqual(route[0], route[-1],)
        self.assertEqual(len(route), len(self.matrix) + 1)
        self.assertEqual(len(set(route[:-1])), len(self.matrix))

    def test_single_city(self):
        self.assertEqual(brute_force([[0]]), (0, [0,0]))
        self.assertEqual(held_karp([[0]]), (0, [0,0]))
        self.assertEqual(nearest_neighbor([[0]]), (0, [0,0]))

if __name__ == "__main__":
    unittest.main()
