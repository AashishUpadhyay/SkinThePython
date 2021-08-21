from src.knapsack import Knapsack


def test1():
    ks = Knapsack()
    assert True == ks.can_partition_dp([1, 5, 11, 5])


def test2():
    ks = Knapsack()
    assert False == ks.can_partition_dp([1, 2, 3, 5])


def test3():
    ks = Knapsack()
    assert True == ks.can_partition_dp([1, 2, 3, 5, 1])


def test4():
    ks = Knapsack()
    assert True == ks.can_partition_dp([1, 1])


def test5():
    ks = Knapsack()
    assert False == ks.can_partition_dp([1, 2, 5])


def test6():
    ks = Knapsack()
    assert False == ks.can_partition_dp([2, 2, 3, 5])


def test7():
    ks = Knapsack()
    assert False == ks.can_partition_dp([1, 3, 4, 4])


def test8():
    ks = Knapsack()
    assert False == ks.can_partition_dp([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                                         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97])


def test9():
    ks = Knapsack()
    assert True == ks.can_partition_dp([72, 77, 17, 63, 79, 95, 57, 40, 82, 39, 77, 20, 91, 41, 66, 78, 69, 94, 28, 2, 48, 35, 40, 32, 34, 65, 18, 56, 71, 15, 28, 18, 43, 41, 41, 50, 2, 86, 77, 11, 62, 56, 91, 77, 56, 61,
                                        63, 39, 31, 52, 48, 65, 96, 97, 37, 50, 36, 88, 82, 75, 14, 41, 36, 12, 68, 1, 60, 1, 1, 40, 34, 75, 27, 73, 100, 13, 92, 93, 60, 64, 60, 65, 66, 56, 3, 63, 95, 3, 83, 73, 65, 73, 7, 63, 58, 57, 34, 26, 78, 99])


def test10():
    ks = Knapsack()
    assert True == ks.can_partition_dp([4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16, 20, 20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40,
                                        40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 48, 48, 48, 48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72, 76, 76, 76, 76, 76, 76, 76, 76, 80, 80])


def test11():
    ks = Knapsack()
    assert False == ks.can_partition_dp([4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16, 20, 20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 48, 48, 48, 48, 48, 48, 48,
                                        48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72, 76, 76, 76, 76, 76, 76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88, 88, 88, 88, 88, 92, 92, 92, 92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99])


def test12():
    ks = Knapsack()
    assert True == ks.can_partition_dp([2, 2, 1, 1])
