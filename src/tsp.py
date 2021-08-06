from sys import path
import copy


class TravelingSalesmanProblem:
    def __init__(self) -> None:
        pass

    def shortest_path(self, graph):
        adj_list = {}
        self.dp = {}

        self.nodes = []
        for i, row in enumerate(graph):
            adj_list[i] = set(row)
            self.nodes.append(i)

        if len(self.nodes) == 1:
            return 0

        self.max_len = len(self.nodes) * (len(self.nodes) - 1)
        result = self.max_len

        for k in self.nodes:
            path_visited = set()
            nodes_visited = f'{0:0{len(self.nodes)}b}'
            received_result = self.dfs(
                k, adj_list, path_visited, nodes_visited)
            result = min(received_result, result)

        return result - 1

    def dfs(self, node, graph, path_visited, nodes_visited):

        if int(nodes_visited, 2) == (pow(2, len(self.nodes)) - 1):
            return 0

        nbours = graph[node]
        nodes_visited = int(nodes_visited, 2) | (1 << node)
        nodes_remaining = nodes_visited ^ (pow(2, len(self.nodes)) - 1)
        key_str = f'{nodes_visited:0{len(self.nodes)}b}-{nodes_remaining:0{len(self.nodes)}b}'

        if node not in self.dp:
            self.dp[node] = {}

        if key_str in self.dp[node]:
            return self.dp[node][key_str]

        ret_val = self.max_len
        for nb in nbours:
            path = str(node) + "-" + str(nb)
            rec_result = None
            if path in path_visited:
                continue

            path_visited.add(path)
            rec_result = self.dfs(
                nb, graph, path_visited, f'{nodes_visited:0{len(self.nodes)}b}')
            path_visited.remove(path)

            ret_val = min(ret_val, (rec_result+1))

        if ret_val != self.max_len:
            self.dp[node][key_str] = ret_val
        return ret_val
