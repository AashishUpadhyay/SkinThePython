from src.datastructures.disjointset import DisjoinSet


class KruskalsAlgorithm:
    def __init__(self) -> None:
        pass

    def minimumSpanningTreeCost(self, n, connections):
        cost = 0
        djs = DisjoinSet()
        connections_sorted = sorted(connections, key=lambda k: k[2])
        total = 0
        for conn in connections_sorted:
            if djs.union(conn[0], conn[1]):
                cost += conn[2]
                total += 1

        if total == n - 1:
            return cost

        return -1
