import heapq


class CheapestItinerary:
    def __init__(self, routes):
        self._graph = self._buildGraph(routes)

    def _buildGraph(self, routes):
        graph = {}
        for r in routes:
            if r[0] not in graph:
                graph[r[0]] = []

            graph[r[0]].append([r[1], r[2]])
        return graph

    def findCheapestPrice(self, src, dest, k):
        q = []
        heapq.heapify(q)
        heapq.heappush(q, [0, src, 0])

        while q:
            dqed = heapq.heappop(q)

            if dqed[1] == dest:
                return dqed[0]

            nbours = self._graph[dqed[1]]

            for n in nbours:
                if (dqed[2] + 1) <= k:
                    heapq.heappush(q, [dqed[0] + n[1], n[0], dqed[2] + 1])

        return -1
