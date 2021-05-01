class ArbitraryQueueUsingFixedLengthArray:
    def __init__(self, array_size):
        self._heads = [None] * array_size
        self._tails = [self._heads]
        
        self._array_size = array_size
        self._size = 0
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        tail_arr_index = len(self._tails) - 1
        self._tails[tail_arr_index][self._tail] = item

        if self._tail == self._array_size-1:
            self._tails.append([None] * self._array_size)
            self._tail = 0
        else:
            self._tail+=1
        self._size+=1
        return 1

    def dequeue(self):

        if self._size == 0:
            return -1

        result = self._heads[self._head]
        if self._head == self._array_size-1:
            self._tails.pop(0)
            self._heads = self._tails[0]
            self._head = 0
        else:
            self._head += 1

        self._size-=1    
        return result    

    def qsize(self):
        return self._size

        






        