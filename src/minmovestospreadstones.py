import itertools


class MinMovesToSpreadStones:
    def __init__(self) -> None:
        pass

    def move(self, grid):
        zero_cells = []
        cells_with_extra_stones = []

        cell_id_cood_map = {}
        cood_cell_id_map = {}

        st = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                st += 1
                cell_id_cood_map[st] = (i, j)
                cood_cell_id_map[(i, j)] = st

                if grid[i][j] == 0:
                    zero_cells.append((i, j))

                if grid[i][j] > 1:
                    for _ in range(grid[i][j]-1):
                        cells_with_extra_stones.append((i, j))

        cell_id_permutations = self._make_permutations(
            [cood_cell_id_map[cell] for cell in zero_cells], [cood_cell_id_map[cell] for cell in cells_with_extra_stones])

        rv = float('inf')
        for permuation in cell_id_permutations:
            cost = 0
            for item in permuation:
                sx, sy = cell_id_cood_map[item[0]
                                          ][0], cell_id_cood_map[item[0]][1]
                ex, ey = cell_id_cood_map[item[1]
                                          ][0], cell_id_cood_map[item[1]][1]
                cost += abs(ex-sx) + abs(ey-sy)
            rv = min(rv, cost)
        return rv

    def _make_permutations(self, list1, list2):
        permutations = itertools.permutations(list2, len(list2))
        result = []
        for perm in permutations:
            result.append(list(zip(list1, perm)))
        return result
