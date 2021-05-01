from src.timekeydictionary import *


def test1():
    tkd = TimeKeyDictionary()

    tkd.set_value(1, 1, 0)
    tkd.set_value(1, 2, 2)

    assert tkd.get_value(1, 1) == 1
    assert tkd.get_value(1, 3) == 2


def test_binary_search():
    li = [0, 2]
    tkd = TimeKeyDictionary()
    assert tkd.binary_search(3, li) == 1
    li = [2, 4, 7]
    assert tkd.binary_search(1, li) == -1
    assert tkd.binary_search(3, li) == 0
    assert tkd.binary_search(5, li) == 1
    assert tkd.binary_search(8, li) == 2


def test2():
    tkd = TimeKeyDictionary()

    tkd.set_value(1, 1, 5)

    assert tkd.get_value(1, 0) == None
    assert tkd.get_value(1, 10) == 1


def test3():
    tkd = TimeKeyDictionary()

    tkd.set_value(1, 1, 0)
    tkd.set_value(1, 2, 0)

    assert tkd.get_value(1, 0) == 2
