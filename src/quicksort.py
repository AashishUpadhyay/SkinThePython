class QuickSort:
    def __init__(self) -> None:
        pass

    def sort(self, arr):
        self.arr = arr
        self.sort_internal(0, len(self.arr)-1)
        return self.arr

    def sort_internal(self, si, ei):
        if si >= ei:
            return

        i = si
        j = si
        pivot_index = ei

        while j<ei:
            if self.arr[j] < self.arr[pivot_index]:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i+=1
                
            j+=1

        if self.arr[i] > self.arr[j]:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.sort_internal(si, i-1)
        self.sort_internal(i+1, ei)
