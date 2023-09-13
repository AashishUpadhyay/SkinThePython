from src.binarysearch import BinarySearch


def test1():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 1) == 0


def test2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 2) == 1


def test3():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 3) == 2


def test4():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 4) == 3


def test5():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 5) == 4


def test6():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 6) == 5


def test7():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 7) == 6


def test8():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 8) == 7


def test9():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 9) == 8


def test10():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 10) == 9


def test11():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, -1) == -1


def test12():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch()
    assert bs.search(lst, 22) == -1


def test13():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 10) == 0


def test13():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 10) == 0


def test14():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 15) == 1


def test15():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 21) == 2


def test16():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 28) == 3


def test17():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 36) == 4


def test18():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 45) == 5


def test19():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 55) == 6


def test20():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 66) == 7


def test21():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 78) == 8


def test22():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 81) == 9


def test23():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 13) == -1


def test24():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 17) == -1


def test25():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 23) == -1


def test26():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 31) == -1


def test27():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 40) == -1


def test28():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 48) == -1


def test29():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 60) == -1


def test30():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 70) == -1


def test31():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 80) == -1


def test32():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 85) == -1


def test31():
    lst = [10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
    bs = BinarySearch()
    assert bs.search(lst, 4) == -1


def test32():
    lst = [1, 2, 5, 8, 11, 13, 14, 21, 22, 25]
    bs = BinarySearch()
    assert bs.search(lst, 0) == -1
    assert bs.search(lst, 1) == 0
    assert bs.search(lst, 25) == 9
    assert bs.search(lst, 5) == 2
    assert bs.search(lst, 21) == 7


def test33():
    lst = [
        3785,
        4392,
        5352,
        5568,
        6020,
        6071,
        8678,
        8817,
        9621,
        10388,
        10720,
        16019,
        17421,
        18625,
        19859,
        20102,
        21712,
        22008,
        22372,
        26419,
        27168,
        27238,
        27679,
        32825,
        32906,
        33468,
        33784,
        33856,
        34634,
        35531,
        36212,
        37930,
        38766,
        39223,
        39257,
        43770,
        45569,
        46229,
        47024,
        47306,
        47480,
        48375,
        51187,
        52268,
        52536,
        53144,
        53411,
        60065,
        61198,
        61912,
        64015,
        65697,
        66550,
        76923,
        76938,
        77451,
        78574,
        78883,
        79249,
        81207,
        82378,
        82736,
        83746,
        84080,
        84212,
        88860,
        88886,
        89921,
        90080,
        93697,
        95879,
        97786,
        98212,
        101521,
        102189,
        105324,
        106730,
        109175,
        113404,
        1422300,
        1423472,
        1426476,
        1427831,
        1432237,
        1433798,
        1434922,
        1435498,
        1436591,
        1436940,
        1442715,
        1443312,
        1444422,
        1447335,
        1447837,
        1448533,
        1452248,
        1453134,
        1453823,
        1454148,
        1454319,
        1454445,
        1457345,
        1700836,
        1703452,
        1704150,
        1704305,
        1706850,
        1707069,
        1712140,
        1712411,
        1713563,
        1715917,
        1716664,
        1718563,
        1721211,
        1722680,
        1722794,
        1722877,
        9914587,
        9916147,
        9917645,
        9918618,
        9919748,
        9927825,
        9929026,
        9929081,
        9929704,
        9930617,
        9930852,
        9932145,
        9933333,
        9934767,
        9935588,
        9935833,
        9936950,
        9940161,
        9943534,
        9945363,
        9946423,
        9949522,
        9950328,
        9951138,
        9955358,
        9958961,
        9962488,
        9963569,
        9965173,
        9965666,
        9966402,
        9967354,
        9968582,
        9968941,
        9970271,
        9970659,
        9971049,
        9971298,
        9975157,
        9976806,
        9980085,
        9980463,
        9980716,
        9981783,
        9982678,
        9983274,
        9983921,
        9986428,
        9986835,
        9987453,
        9988108,
        9988632,
        9988841,
        9988984,
        9993664,
        9996663,
        9997458,
        9998970,
    ]
    bs = BinarySearch()
    assert bs.search(lst, 3780) == -1
    assert bs.search(lst, 3785) == 0
    assert bs.search(lst, 9868243) == -1
    assert bs.search(lst, 9997458) == 174
    assert bs.search(lst, 9998970) == 175
