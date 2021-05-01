class FixedSizeQueue:
    def __init__(self, size):
        self._head = 0
        self._tail = 0
        self._items = [None] * size
        self._limit = size

    def enqueue(self, item):
        if self.qsize() == self._limit:
            return -1

        self._items[self._tail] = item

        if self._tail == self._limit-1:
            self._tail = 0
        else:
            self._tail += 1
        return 1    

    def dequeue(self):
        if self.qsize() == 0:
            return -1

        result = self._items[self._head]
        self._items[self._head] = None

        if self._head == self._limit-1:
            self._head = 0
        else:
            self._head += 1

        return result

    def qsize(self):

        if self._tail > self._head:
            return self._tail - self._head
        elif self._tail < self._head:  
            return (self._tail - 0) + (self._limit - self._head)
        else:
            if self._head != (self._limit - 1) and self._items[self._head+1] != None:
                return self._limit
            elif self._tail != 0 and self._items[self._tail-1] != None:     
                return self._limit
            else:
                return 0    
