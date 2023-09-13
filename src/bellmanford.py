class BellmanFord:
    def __init__(self) -> None:
        pass

    def shortest_path(self, graph, start):
        # Relax all edges for N-1 times
        # where N is the number of nodes
        result = [100000] * len(graph)
        result[start] = 0

        for _ in range(len(graph) - 1):
            for ri, row in enumerate(graph):
                for col in row:
                    if result[col[0]] > result[ri] + col[1]:
                        result[col[0]] = result[ri] + col[1]

        return result
