import unittest
from src.trainhard.minimum_time_to_transport_all_individuals import Solution


class TestMinTimeToTransportAllIndividuals(unittest.TestCase):
    def test_minimum_time_to_transport_all_individuals1(self):
        sol = Solution()
        self.assertEqual(sol.minTime(
            1, 1, 2, [5], [1.0, 1.3]), 5)

    def test_minimum_time_to_transport_all_individuals2(self):
        sol = Solution()
        self.assertEqual(sol.minTime(
            3, 2, 3, [2, 5, 8], [1.0, 1.5, 0.75]), 14.5)
        pass

    def test_minimum_time_to_transport_all_individuals3(self):
        sol = Solution()
        self.assertEqual(sol.minTime(
            2, 1, 2, [10, 10], [2.0, 2.0]), -1)
        pass

    def test_minimum_time_to_transport_all_individuals4(self):
        sol = Solution()
        self.assertEqual(sol.minTime(
            3, 2, 4, [57, 80, 46], [1.37, 1.81, 0.52, 1.66]), 240.53000)
        pass
