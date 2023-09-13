import pprint
import unittest
from src.minmovestospreadstones import MinMovesToSpreadStones


class TestMinMovesToSpreadStones(unittest.TestCase):
    def setup(self):
        pass

    def tests(self):
        grids_and_expected_values = [
            [[[1, 1, 0], [1, 1, 1], [1, 2, 1]], 3],
            [[[1, 3, 0], [1, 0, 0], [1, 0, 3]], 4],
            [[[3, 2, 0], [0, 1, 0], [0, 3, 0]], 7],
            [[[1, 2, 2], [1, 1, 0], [0, 1, 1]], 4],
            [[[1, 3, 3], [1, 0, 0], [0, 1, 0]], 7]
        ]

        for grid in grids_and_expected_values:
            assert self._runtests(grid[0]) == grid[1]

    def _runtests(self, grid):
        min_moves_to_spread_stones = MinMovesToSpreadStones()
        return min_moves_to_spread_stones.move(grid)

    def test___make_permutations(self):
        min_moves_to_spread_stones = MinMovesToSpreadStones()
        grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]
        cell_id_cood_map = {}
        cood_cell_id_map = {}

        st = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                st += 1
                cell_id_cood_map[st] = (i, j)
                cood_cell_id_map[(i, j)] = st

        zero_cells = [(0, 2), (1, 1), (1, 2), (2, 1)]
        cells_with_extra_stones = [(0, 1), (0, 1), (2, 2), (2, 2)]

        cell_id_permutations = min_moves_to_spread_stones._make_permutations(
            [cood_cell_id_map[cell] for cell in zero_cells], [cood_cell_id_map[cell] for cell in cells_with_extra_stones])

        cell_permutations = []
        for permuation in cell_id_permutations:
            cell_permutation = []
            for item in permuation:
                cell_permutation.append(
                    [cell_id_cood_map[item[0]], cell_id_cood_map[item[1]]])
            cell_permutations.append(cell_permutation)
        # pp = pprint.PrettyPrinter()
        # pp.pprint(cell_permutations)
        assert len(cell_permutations) == 24
