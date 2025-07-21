import unittest
from src.trainhard.combinations import Solution


class TestCombinations(unittest.TestCase):
    def test_combinations1(self):
        sol = Solution()
        received = sol.generate_combinations(
            [1, 2, 3], 2)
        print(received)
        self.assertEqual(received, [[1, 2], [1, 3], [2, 3]])
        pass

    def test_combinations2(self):
        sol = Solution()
        received = sol.generate_combinations(
            [1, 2, 3], 3)
        print(received)
        self.assertEqual(received, [[1, 2, 3]])
        pass

    def test_single_item_combinations(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2, 3, 4], 1)
        self.assertEqual(received, [[1], [2], [3], [4]])

    def test_all_items_combination(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2, 3, 4], 4)
        self.assertEqual(received, [[1, 2, 3, 4]])

    def test_empty_list(self):
        sol = Solution()
        received = sol.generate_combinations([], 0)
        self.assertEqual(received, [])

    def test_non_sequential_numbers(self):
        sol = Solution()
        received = sol.generate_combinations([5, 10, 15], 2)
        self.assertEqual(received, [[5, 10], [5, 15], [10, 15]])

    def test_larger_combination(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2, 3, 4, 5], 3)
        expected = [[1, 2, 3], [1, 2, 4], [1, 2, 5],
                    [1, 3, 4], [1, 3, 5], [1, 4, 5],
                    [2, 3, 4], [2, 3, 5], [2, 4, 5],
                    [3, 4, 5]]
        self.assertEqual(received, expected)

    def test_r_greater_than_n(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2], 3)
        self.assertEqual(received, [])

    def test_zero_items(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2, 3], 0)
        self.assertEqual(received, [])

    def test_large_numbers(self):
        sol = Solution()
        received = sol.generate_combinations([1000000, 2000000, 3000000], 2)
        self.assertEqual(received, [[1000000, 2000000], [
                         1000000, 3000000], [2000000, 3000000]])

    def test_negative_numbers(self):
        sol = Solution()
        received = sol.generate_combinations([-1, -2, -3], 2)
        self.assertEqual(received, [[-1, -2], [-1, -3], [-2, -3]])

    def test_mixed_numbers(self):
        sol = Solution()
        received = sol.generate_combinations([-1, 0, 1], 2)
        self.assertEqual(received, [[-1, 0], [-1, 1], [0, 1]])

    def test_negative_r(self):
        sol = Solution()
        received = sol.generate_combinations([1, 2, 3], -1)
        self.assertEqual(received, [])

    def test_empty_list_nonzero_r(self):
        sol = Solution()
        received = sol.generate_combinations([], 2)
        self.assertEqual(received, [])

    def test_single_item_list(self):
        sol = Solution()
        received = sol.generate_combinations([42], 1)
        self.assertEqual(received, [[42]])

    def test_duplicate_numbers(self):
        sol = Solution()
        received = sol.generate_combinations([1, 1, 2], 2)
        self.assertEqual(received, [[1, 1], [1, 2], [1, 2]])

    def test_non_numeric_items(self):
        sol = Solution()
        received = sol.generate_combinations(['a', 'b', 'c'], 2)
        self.assertEqual(received, [['a', 'b'], ['a', 'c'], ['b', 'c']])

    def test_mixed_types(self):
        sol = Solution()
        received = sol.generate_combinations([1, 'a', True], 2)
        self.assertEqual(received, [[1, 'a'], [1, True], ['a', True]])
