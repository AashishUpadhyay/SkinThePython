from src.americancrosswordpuzzle import *

def test__validate_word_min_length_internal1():
    grid = [[0,0,0,1,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length_internal(grid)

def test__validate_word_min_length_internal2():
    grid = [[0,0,1,1,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length_internal(grid) == False

def test__validate_word_min_length_internal3():
    grid = [[0,0,0,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length_internal(grid)

def test__validate_word_min_length_internal4():
    grid = [[0,0,0,1,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length_internal(grid) == False

def test__transpose1():
    grid = [[0,0,0,1,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    transpose = acp._transpose(grid)
    assert len(transpose) == 6
    assert transpose[0][0] == 0
    assert transpose[1][0] == 0
    assert transpose[2][0] == 0
    assert transpose[3][0] == 1
    assert transpose[4][0] == 1
    assert transpose[5][0] == 1

def test__transpose2():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    transpose = acp._transpose(grid)
    assert len(transpose) == 6
    assert transpose[0][0] == 0
    assert transpose[1][0] == 0
    assert transpose[2][0] == 0
    assert transpose[3][0] == 1
    assert transpose[4][0] == 1
    assert transpose[5][0] == 1

    assert transpose[0][1] == 0
    assert transpose[1][1] == 1
    assert transpose[2][1] == 0
    assert transpose[3][1] == 1
    assert transpose[4][1] == 0
    assert transpose[5][1] == 1

    assert transpose[0][2] == 1
    assert transpose[1][2] == 1
    assert transpose[2][2] == 0
    assert transpose[3][2] == 0
    assert transpose[4][2] == 1
    assert transpose[5][2] == 1

def test__validate_word_min_length1():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length(grid) == False

def test__validate_word_min_length2():
    grid = [[0,0,0,1,1,1],[1,1,1,0,0,0],[1,0,0,0,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length(grid) == False

def test__validate_word_min_length3():
    grid = [[0,0,0,1,1,1],[0,0,0,1,1,1],[0,0,0,1,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length(grid)

def test__validate_word_min_length4():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_word_min_length(grid)

def test__reverse1():
    grid = [[0,0,0,1,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    reverse = acp._reverse(grid)
    assert grid[0] == reverse[0]

def test__reverse2():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    reverse = acp._reverse(grid)
    assert grid[0] == reverse[2]
    assert grid[1] == reverse[1]
    assert grid[2] == reverse[0]

def test__validate_rotational_symmetry1():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_rotational_symmetry(grid) == False

def test__validate_rotational_symmetry2():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_rotational_symmetry(grid)

def test__validate_rotational_symmetry3():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,1,1,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_rotational_symmetry(grid)

def test__count_all_empty_cells():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,1,1,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._count_all_empty_cells(grid) == 12

def test__is_valid_cell():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,1,1,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._is_valid_cell(2,2, grid)

def test__is_valid_cell2():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,1,1,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._is_valid_cell(-1,2, grid) == False

def test__is_valid_cell3():
    grid = [[0,0,0,1,1,1],[0,1,0,1,0,1],[1,0,1,0,1,0],[1,1,1,0,0,0]]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._is_valid_cell(4,2, grid) == False

def test__get_cell_id():
    grid = []
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._get_cell_id(4,2) == "4_2"

def test__count_all_connected_empty_cells():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._count_all_connected_empty_cells(grid) == 98

def test__count_all_empty_cells1():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._count_all_empty_cells(grid) == 98

def test__validate_all_empty_cells_are_connected():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp._validate_all_empty_cells_are_connected(grid) 

def test_valid():
    grid = [
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        ]
    acp = AmericanCrosswordPuzzle(grid)
    assert acp.valid()

    