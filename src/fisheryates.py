import random
class FisherYates:
    def __init__(self) -> None:
        pass

    def shuffle(self, arr):
        for k in range(len(arr)-1, 0, -1):
            j = random.randrange(0, k+1) 
            arr[k], arr[j] = arr[j], arr[k]
        return arr                
