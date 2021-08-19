class FLoydWarshall:
    def __init__(self) -> None:
        pass

    def build_all_pair_shortest_path(self, graph):

        dp = [[10000 for _ in range(len(graph))] for _ in range(len(graph))]
        path = [['N' for _ in range(len(graph))] for _ in range(len(graph))]

        for ri, row in enumerate(graph):
            dp[ri][ri] = 0
            for col in row:
                dp[ri][col[0]] = col[1]
                path[ri][col[0]] = col[0]

        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if dp[i][j] > dp[i][k] + dp[k][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        path[i][j] = k

        return dp
