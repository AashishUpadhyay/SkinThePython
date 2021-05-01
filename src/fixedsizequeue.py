class FixedSizeQueue:
    def __init__(self, size):
        self._head = 0
        self._tail = 0
        self._items = [None] * size
        self._limit = size
        self._size = 0

    def enqueue(self, item):
        if self.qsize() == self._limit:
            return -1

        self._items[self._tail] = item

        if self._tail == self._limit - 1:
            self._tail = 0
        else:
            self._tail += 1

        self._size += 1
        return 1

    def dequeue(self):
        if self.qsize() == 0:
            return -1

        result = self._items[self._head]
        self._items[self._head] = None

        if self._head == self._limit - 1:
            self._head = 0
        else:
            self._head += 1

        self._size -= 1

        return result

    def qsize(self):
        return self._size
