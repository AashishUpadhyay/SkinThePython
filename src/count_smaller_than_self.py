from src.datastructures.fenwicktree import FenwickTree
class CountSmallerThanSelf:
    def __init__(self) -> None:
        pass

    def count(self, input):
        offset = 10000
        fw = FenwickTree()
        tree = [0 for _ in range(10000 + 1 + 10001)]
        result = [0 for _ in range(len(input))]
        for i in range(len(input)-1, -1, -1):
            result[i] = fw.query(offset + input[i], tree)
            fw.update(offset + input[i], 1, tree)
        return result