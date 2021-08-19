from src.floyd_warshall import FLoydWarshall


def test():
    graph = [
        [[1, 9], [2, 3]],
        [[2, 6], [4, 2]],
        [[1, 2], [3, 1]],
        [[2, 2], [4, 2]],
        []]

    fw = FLoydWarshall()
    received = fw.build_all_pair_shortest_path(graph)

    expected = [
        [0, 5, 3, 4, 6],
        [10000, 0, 6, 7, 2],
        [10000, 2, 0, 1, 3],
        [10000, 4, 2, 0, 2],
        [10000, 10000, 10000, 10000, 0]
    ]

    for i, row in enumerate(expected):
        for j in range(len(row)):
            if expected[i][j] != received[i][j]:
                assert False

    assert True
