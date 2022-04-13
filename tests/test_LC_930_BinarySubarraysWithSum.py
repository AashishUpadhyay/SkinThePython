from src.LC_930_BinarySubarraysWithSum import LC_930_BinarySubarraysWithSum


def test1():
    problem = LC_930_BinarySubarraysWithSum()
    assert 4 == problem.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
