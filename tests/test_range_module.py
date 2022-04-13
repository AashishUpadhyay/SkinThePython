from src.rangemodule import RangeModule


def test1():
    rm = RangeModule()
    rm.addRange(1, 3)
    rm.addRange(9, 11)
    rm.addRange(15, 20)
    rm.addRange(1, 16)
