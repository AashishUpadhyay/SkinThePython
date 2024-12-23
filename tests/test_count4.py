from src.count4 import Count4


def test1():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[0][1] = "R"
    count4.arr[0][2] = "R"
    count4.arr[0][3] = "R"

    assert count4.horCnt([0, 3], "R") == 4


def test2():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[1][0] = "R"
    count4.arr[2][0] = "R"
    count4.arr[3][0] = "R"

    assert count4.verCnt([3, 0], "R") == 4


def test3():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[1][1] = "R"
    count4.arr[2][2] = "R"
    count4.arr[3][3] = "R"

    assert count4.diaCnt([3, 3], "R") == 4


def test4():
    count4 = Count4()

    count4.arr[0][5] = "R"
    count4.arr[1][4] = "R"
    count4.arr[2][3] = "R"
    count4.arr[3][2] = "R"

    assert count4.diaCnt([3, 2], "R") == 4


def test5():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[1][1] = "R"
    count4.arr[2][2] = "R"
    count4.arr[3][3] = "R"

    assert count4.diaCnt([0, 0], "R") == 4


def test6():
    count4 = Count4()

    count4.arr[0][5] = "R"
    count4.arr[1][4] = "R"
    count4.arr[2][3] = "R"
    count4.arr[3][2] = "R"

    assert count4.diaCnt([0, 5], "R") == 4


def test7():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[0][1] = "R"
    count4.arr[0][2] = "R"
    count4.arr[0][3] = "R"

    assert count4.horCnt([0, 1], "R") == 4


def test8():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[1][0] = "R"
    count4.arr[2][0] = "R"
    count4.arr[3][0] = "R"

    assert count4.verCnt([2, 0], "R") == 4


def test9():
    count4 = Count4()

    count4.arr[0][0] = "R"
    count4.arr[1][1] = "R"
    count4.arr[2][2] = "R"
    count4.arr[3][3] = "R"

    assert count4.diaCnt([1, 1], "R") == 4


def test10():
    count4 = Count4()

    count4.arr[0][5] = "R"
    count4.arr[1][4] = "R"
    count4.arr[2][3] = "R"
    count4.arr[3][2] = "R"

    assert count4.diaCnt([2, 3], "R") == 4
