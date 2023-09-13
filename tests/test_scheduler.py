from src.Scheduler import Scheduler


def test1():
    sc = Scheduler()
    input = [[1, 2], [1.5, 2.5], [2, 2.5]]
    assert 2 == sc.number_of_docks(input)


def test2():
    sc = Scheduler()
    input = [[1, 2], [1.5, 2.5], [1.75, 2.5]]
    assert 3 == sc.number_of_docks(input)


def test3():
    sc = Scheduler()
    input = [[1, 2], [0.5, 2.5], [1.75, 2.5]]
    assert 3 == sc.number_of_docks(input)
