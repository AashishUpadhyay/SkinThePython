import unittest
from src.trainhard.longest_palindromic_path_in_graph import Solution


class TestLongestPalindromicPathInGraph(unittest.TestCase):
    def test_longest_palindromic_path_in_graph1(self):
        sol = Solution()
        self.assertEqual(sol.maxLen(
            4, [[0, 1], [1, 2], [2, 3]], "abba"), 4)

    def test_longest_palindromic_path_in_graph2(self):
        sol = Solution()
        self.assertEqual(sol.maxLen(
            14, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                 [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [1, 2],
                 [1, 3], [1, 4], [1, 5], [1, 6], [
                1, 7], [1, 8], [1, 9], [1, 10],
                [1, 11], [1, 12], [1, 13], [2, 3], [
                2, 4], [2, 5], [2, 6], [2, 7],
                [2, 8], [2, 9], [2, 10], [2, 11], [
                2, 12], [2, 13], [3, 4], [3, 5],
                [3, 6], [3, 7], [3, 8], [3, 9], [
                3, 10], [3, 11], [3, 12], [3, 13],
                [4, 5], [4, 6], [4, 7], [4, 8], [
                4, 9], [4, 10], [4, 11], [4, 12],
                [4, 13], [5, 6], [5, 7], [5, 8], [
                5, 9], [5, 10], [5, 11], [5, 12],
                [5, 13], [6, 7], [6, 8], [6, 9], [
                6, 10], [6, 11], [6, 12], [6, 13],
                [7, 8], [7, 9], [7, 10], [7, 11], [
                7, 12], [7, 13], [8, 9], [8, 10],
                [8, 11], [8, 12], [8, 13], [9, 10], [
                9, 11], [9, 12], [9, 13], [10, 11],
                [10, 12], [10, 13], [11, 12], [11, 13], [12, 13]], "aaaaaaaaaaaaaa"), 14)
        pass

    def test_longest_palindromic_path_in_graph3(self):
        sol = Solution()
        self.assertEqual(sol.maxLen(
            4, [[0, 1], [1, 2], [2, 3]], "abba"), 4)
        self.assertEqual(sol.maxLen(
            1, [], "z"), 1)

    def test_longest_palindromic_path_in_graph4(self):
        sol = Solution()
        self.assertEqual(sol.maxLen(
            3, [[0, 1], [1, 2]], "aba"), 3)

    def test_longest_palindromic_path_in_graph5(self):
        sol = Solution()
        self.assertEqual(sol.maxLen(
            6, [[0, 2], [0, 3], [1, 2], [2, 3], [5, 1], [0, 5]], "kmolmo"), 3)
        #   l(3)
        #   /   \
        # k(0)---o(2)
        # |       |
        # o(5)---m(1)
