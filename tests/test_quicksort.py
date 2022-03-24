from src.quicksort import QuickSort


def test1():
    qs = QuickSort()
    received = qs.sort([10, 15, 5, 8, 20, 3, 6, 11])
    expected = sorted([10, 15, 5, 8, 20, 3, 6, 11])
    assert received == expected


def test2():
    qs = QuickSort()
    received = qs.sort([20, 15, 11, 10, 8, 6, 5, 3])
    expected = sorted([20, 15, 11, 10, 8, 6, 5, 3])
    assert received == expected


def test3():
    qs = QuickSort()
    received = qs.sort([30, 10, 40, 50])
    expected = sorted([30, 10, 40, 50])
    assert received == expected


def test4():
    qs = QuickSort()
    received = qs.sort([10, 80, 30, 90, 40, 50, 70])
    expected = sorted([10, 80, 30, 90, 40, 50, 70])
    assert received == expected


def test5():
    qs = QuickSort()
    received = qs.sort([2, 2, 2, 2, 3, 2])
    expected = sorted([2, 2, 2, 2, 3, 2])
    assert received == expected
