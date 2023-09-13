from src.bellmanford import BellmanFord


def test():
    graph = [[[1, 9], [2, 3]], [[2, 6], [4, 2]], [[1, 2], [3, 1]], [[2, 2], [4, 2]], []]

    bf = BellmanFord()
    result = bf.shortest_path(graph, 0)

    assert result[0] == 0
    assert result[1] == 5
    assert result[2] == 3
    assert result[3] == 4
    assert result[4] == 6
