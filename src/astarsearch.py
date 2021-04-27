import copy
import heapq


class Solution:
    def __init__(self, arr, endstate):
        self._arr = arr
        self._endstate = endstate
        self._row = len(arr)
        self._col = len(arr[0])

    def Solve8by8(self):

        if self._arr == self._endstate:
            return 0

        for i in range(len(self._arr)):
            for j in range(len(self._arr[i])):

                if self._arr[i][j] > 0:
                    continue

                newarr = copy.deepcopy(self._arr)
                move = self.bfs(newarr, i, j)
                if move:
                    return move

        return -1

    def bfs(self, newarr, i, j):
        seen = set()
        heap = []
        heapq.heappush(heap, (self.distance(newarr), [newarr, [i, j], 0]))

        while heap:

            dqedItem = heapq.heappop(heap)

            dqed = dqedItem[1]

            arr = dqed[0]
            i, j = dqed[1]
            move = dqed[2]

            if arr == self._endstate:
                return move

            arrid = self.id(arr)

            if arrid in seen:
                continue

            seen.add(arrid)

            if self.move(i + 1, j):
                narr = self.switch(arr, i + 1, j, i, j)
                heapq.heappush(
                    heap, (self.distance(narr), [narr, [i + 1, j], move + 1])
                )

            if self.move(i - 1, j):
                narr = self.switch(arr, i - 1, j, i, j)
                heapq.heappush(
                    heap, (self.distance(narr), [narr, [i - 1, j], move + 1])
                )

            if self.move(i, j + 1):
                narr = self.switch(arr, i, j + 1, i, j)
                heapq.heappush(
                    heap, (self.distance(narr), [narr, [i, j + 1], move + 1])
                )

            if self.move(i, j - 1):
                narr = self.switch(arr, i, j - 1, i, j)
                heapq.heappush(
                    heap, (self.distance(narr), [narr, [i, j - 1], move + 1])
                )

        return None

    def bfsbruteforce(self, newarr, i, j):
        seen = set()
        q = []
        q.append([newarr, [i, j], 0])

        while q:
            dqed = q.pop(0)

            arr = dqed[0]
            i, j = dqed[1]
            move = dqed[2]

            if arr == self._endstate:
                return move

            arrid = self.id(arr)

            if arrid in seen:
                continue

            seen.add(arrid)

            if self.move(i + 1, j):
                narr = self.switch(arr, i + 1, j, i, j)
                q.append([narr, [i + 1, j], move + 1])

            if self.move(i - 1, j):
                narr = self.switch(arr, i - 1, j, i, j)
                q.append([narr, [i - 1, j], move + 1])

            if self.move(i, j + 1):
                narr = self.switch(arr, i, j + 1, i, j)
                q.append([narr, [i, j + 1], move + 1])

            if self.move(i, j - 1):
                narr = self.switch(arr, i, j - 1, i, j)
                q.append([narr, [i, j - 1], move + 1])

        return None

    def move(self, i, j):

        if i < 0 or j < 0 or i > self._row - 1 or j > self._col - 1:
            return False

        return True

    def switch(self, arr, ni, nj, oi, oj):
        newarr = copy.deepcopy(arr)
        newarr[oi][oj], newarr[ni][nj] = newarr[ni][nj], newarr[oi][oj]
        return newarr

    def distance(self, arr):
        result = 0

        for i in range(len(self._arr)):
            for j in range(len(self._arr[i])):
                if arr[i][j] > 0 and arr[i][j] != self._endstate[i][j]:
                    result += 1

        return result

    def id(self, arr):
        sb = ""
        lst = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                lst.append(arr[i][j])

        return "-".join(str(i) for i in lst)
