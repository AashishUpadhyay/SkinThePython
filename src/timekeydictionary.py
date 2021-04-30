import heapq


class TimeKeyDictionary:
    def __init__(self):
        self.map = {}

    def set_value(self, k, v, t):
        if k not in self.map:
            self.map[k] = [{}, []]

        time_map, li = self.map[k]
        if t not in time_map:
            heapq.heappush(li, t)
        time_map[t] = v

    def get_value(self, k, t):
        if k not in self.map:
            return None

        time_map, li = self.map[k]

        if t in time_map:
            return time_map[t]

        index = self.binary_search(t, li)

        if index < 0:
            return None

        return time_map[li[index]]

    def binary_search(self, t, li):
        si = 0
        ei = len(li) - 1

        while si != ei:
            mi = si + (ei - si) // 2

            if li[mi] < t:
                si = mi + 1
            else:
                ei = mi - 1

        if si == 0 and li[si] > t:
            return -1

        if li[si] < t and si == len(li) - 1:
            return si

        if li[si] < t:
            return si
        else:
            return si - 1
