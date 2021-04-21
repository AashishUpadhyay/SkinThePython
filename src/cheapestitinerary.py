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
        q = [[src, 0, 0]]

        while q:
            q.sort(key=lambda x:x[1])

            dqed = q.pop(0)

            if dqed[0] == dest:
                return dqed[1]

            nbours = self._graph[dqed[0]]

            for n in nbours:
                if (dqed[2] + 1) <= k:
                    q.append([n[0], dqed[1] + n[1], dqed[2] + 1])

        return -1            
