class Quack:
    def __init__(self):
        self._left = []
        self._right = []
        self._buffer = []
        pass

    def push(self, item):
        self._left.append(item)

    def pop(self):
        if not self._left and not self._right:
            return -1

        if not self._left:
            rt_len = len(self._right)

            for _ in range(rt_len // 2):
                self._buffer.append(self._right.pop())

            while self._right:
                self._left.append(self._right.pop())

            while self._buffer:
                self._right.append(self._buffer.pop())

        return self._left.pop()

    def pull(self):
        if not self._left and not self._right:
            return -1

        if not self._right:
            lf_len = len(self._left)

            for _ in range(lf_len // 2):
                self._buffer.append(self._left.pop())

            while self._left:
                self._right.append(self._left.pop())

            while self._buffer:
                self._left.append(self._buffer.pop())

        return self._right.pop()
