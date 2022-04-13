from src.fisheryates import FisherYates


def test_shuffle():
    fy = FisherYates()
    arr = [11, 2, 13, 234, 225, 36, 17]
    result = fy.shuffle(arr)
