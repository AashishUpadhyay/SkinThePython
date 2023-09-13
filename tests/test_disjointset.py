from src.datastructures.disjointset import DisjoinSet


def test1():
    djs = DisjoinSet()
    djs.union(1, 2)
    djs.union(1, 3)
    djs.union(2, 3)
    djs.union(3, 4)
    djs.union(4, 3)

    djs.union(6, 7)
    djs.union(7, 8)
    djs.union(7, 9)
    djs.union(8, 7)
    djs.union(9, 7)

    assert len(djs.groups) == 2
