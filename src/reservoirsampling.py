import random


class ReservoirSampling:
    def __init__(self) -> None:
        pass

    def select_element_at_random(self, arr):
        result = None
        for i, elem in enumerate(arr):
            if random.randrange(0, i + 1) == 0:
                result = elem
        return result

    def select_k_elements_at_random(self, k, arr):
        res = []
        for i in range(k):
            res.append(arr[i])

        for i in range(k, len(arr)):
            j = random.randrange(0, i + 1)
            if j < k:
                res[j], arr[i] = arr[i], res[j]

        return res
