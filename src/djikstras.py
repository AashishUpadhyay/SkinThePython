class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = self.buildGraph(times)
        ntimesMap = {}
        visited = {}

        q = [[k, 0]]

        while q:
            dqedItem = q.pop(0)

            if dqedItem[0] not in ntimesMap:
                ntimesMap[dqedItem[0]] = dqedItem[1]
            else:
                ntimesMap[dqedItem[0]] = min(ntimesMap[dqedItem[0]], dqedItem[1])

            if dqedItem[0] in graph:
                nbours = graph[dqedItem[0]]

                sortednbours = sorted(nbours, key=lambda x: x[1])

                for nb in sortednbours:
                    edge = str(dqedItem[0]) + "-" + str(nb[0])
                    cost = nb[1] + dqedItem[1]
                    if edge not in visited or visited[edge] > cost:
                        q.append([nb[0], cost])
                        visited[edge] = cost

        ndt = -1

        if len(ntimesMap) < n:
            return ndt

        for mk, mv in ntimesMap.items():
            ndt = max(ndt, mv)

        return ndt

    def buildGraph(self, times):
        graph = {}

        for t in times:
            if t[0] not in graph:
                graph[t[0]] = []

            graph[t[0]].append([t[1], t[2]])

        return graph
