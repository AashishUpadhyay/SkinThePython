import copy


class AmericanCrosswordPuzzle:
    def __init__(self, grid):
        self._grid = grid

    def valid(self):
        return (
            self._validate_word_min_length(self._grid)
            and self._validate_rotational_symmetry(self._grid)
            and self._validate_all_empty_cells_are_connected(self._grid)
        )

    def _validate_word_min_length(self, grid):
        if not self._validate_word_min_length_internal(grid):
            return False

        transpose = self._transpose(grid)

        if not self._validate_word_min_length_internal(transpose):
            return False

        return True

    def _validate_word_min_length_internal(self, grid):
        for row in grid:
            min_word_len = -1
            for col in row:
                if col == 1 and min_word_len == -1:
                    continue

                if col == 0 and min_word_len == -1:
                    min_word_len = 1
                    continue

                if col == 0:
                    min_word_len += 1
                else:
                    if min_word_len < 3:
                        return False
                    else:
                        min_word_len = -1
            if min_word_len > 0 and min_word_len < 3:
                return False
        return True

    def _transpose(self, grid):
        transpose = []

        if len(grid) == 0:
            return transpose

        for ci in range(len(grid[0])):
            row = []
            for ri in range(len(grid)):
                row.append(grid[ri][ci])
            transpose.append(row)
        return transpose

    def _reverse(self, grid):
        reverse = []
        for row in grid:
            reverse.insert(0, copy.deepcopy(row))
        return reverse

    def _validate_rotational_symmetry(self, grid):
        transpose = self._transpose(grid)
        reverse = self._reverse(transpose)
        transpose = self._transpose(reverse)
        reverse = self._reverse(transpose)

        for i in range(len(grid)):
            if not grid[i] == reverse[i]:
                return False
        return True

    def _validate_all_empty_cells_are_connected(self, grid):
        return self._count_all_empty_cells(
            grid
        ) == self._count_all_connected_empty_cells(grid)

    def _count_all_empty_cells(self, grid):
        result = 0
        for row in grid:
            for col in row:
                if col == 0:
                    result += 1
        return result

    def _count_all_connected_empty_cells(self, grid):
        done = False
        for ri in range(len(grid)):
            for ci in range(len(grid[0])):
                if grid[ri][ci] == 0:
                    done = True
                    break
            if done:
                break
        seen = set()
        empty = set()
        self._dfs(ri, ci, grid, seen, empty)
        return len(empty)

    def _dfs(self, ri, ci, grid, seen, empty):
        if not self._is_valid_cell(ri, ci, grid):
            return

        cell_id = self._get_cell_id(ri, ci)

        if cell_id in seen:
            return

        seen.add(cell_id)

        if grid[ri][ci] == 0:
            empty.add(cell_id)

        self._dfs(ri - 1, ci, grid, seen, empty)
        self._dfs(ri + 1, ci, grid, seen, empty)
        self._dfs(ri, ci - 1, grid, seen, empty)
        self._dfs(ri, ci + 1, grid, seen, empty)

    def _is_valid_cell(self, ri, ci, grid):
        if ri < 0 or ri > len(grid) - 1:
            return False

        if ci < 0 or ci > len(grid[0]) - 1:
            return False

        return True

    def _get_cell_id(self, ri, ci):
        return f"{ri}_{ci}"
