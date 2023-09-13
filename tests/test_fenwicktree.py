from typing import Collection
from src.datastructures.fenwicktree import FenwickTree


def test1():
    fw = FenwickTree()
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    received = fw.create(input)
    expected = [1, 3, 3, 10, 5, 11, 7, 36, 9, 19]
    for i in range(len(received)):
        assert received[i] == expected[i]


def test2():
    fw = FenwickTree()
    input = [1, 3, 3, 10, 5, 11, 7, 36, 9, 19]
    fw.update(4, 5, input)
    expected = [1, 3, 3, 10, 10, 16, 7, 41, 9, 19]
    for i in range(len(input)):
        assert input[i] == expected[i]


def test3():
    fw = FenwickTree()
    input = [1, 3, 3, 10, 5, 11, 7, 36, 9, 19]
    received = fw.query(10, input)
    assert 55 == received
    received = fw.query(9, input)
    assert 45 == received
    received = fw.query(8, input)
    assert 36 == received
    received = fw.query(4, input)
    assert 10 == received
