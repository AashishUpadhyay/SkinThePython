from src.tsp import TravelingSalesmanProblem


def test1():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1, 2, 3], [0], [0], [0]])
    # [1,0,2,0,3]
    assert result == 4


def test2():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
    # [0,1,4,2,3]
    assert result == 4


def test3():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs(
        [
            [7],
            [3],
            [3, 9],
            [1, 2, 4, 5, 7, 11],
            [3],
            [3],
            [9],
            [3, 10, 8, 0],
            [7],
            [11, 6, 2],
            [7],
            [3, 9],
        ]
    )
    assert result == 17


def test4():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ]
    )
    assert result == 11


def test5():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[]])
    assert result == 0


def test6():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2, 4], [1, 3], [2], [1]])
    assert result == 5


def test7():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]])
    assert result == 6


def test8():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2], [1, 3], [2]])
    assert result == 3


def test9():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2], [1, 3], [2]])
    assert result == 3


def test10():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[1], [0, 2, 4], [1, 3], [2], [1]])
    assert result == 5


def test11():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs([[2, 3], [6, 5], [0, 6], [0, 4], [3], [1], [2, 1]])
    assert result == 6


def test12():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs(
        [[2, 3], [7], [0, 6], [0, 4, 7], [3, 8], [7], [2], [5, 3, 1], [4]]
    )
    assert result == 11


def test13():
    tsp = TravelingSalesmanProblem()
    result = tsp.shortest_path_bfs(
        [
            [6, 9],
            [6, 8],
            [6, 7],
            [6, 10],
            [8],
            [10],
            [0, 1, 2, 3, 8],
            [2, 8, 9],
            [1, 4, 6, 7],
            [0, 7, 10],
            [3, 5, 9],
        ]
    )
    assert result == 11
