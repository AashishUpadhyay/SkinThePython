class FenwickTree:
    def __init__(self) -> None:
        pass

    def create(self, arr):
        tree = [0 for _ in range(len(arr))]
        for i, v in enumerate(arr):
            self.update(i, v, tree)    
        return tree    

    def query(self, count, tree):
        result = 0
        while count >0:
            result+= tree[count-1]
            count &= count - 1
        return result    

    def update(self, index, val, tree):
        while index < len(tree):
            tree[index] += val
            index |= index + 1
