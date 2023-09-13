from sys import path
import copy


class TravelingSalesmanProblem:
    def __init__(self) -> None:
        pass

    def shortest_path(self, graph):
        adj_list = {}
        self.memo = {}

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
            nodes_visited = f"{0:0{len(self.nodes)}b}"
            received_result = self.dfs(k, adj_list, path_visited, nodes_visited)
            result = min(received_result, result)

        return result - 1

    def dfs(self, node, graph, path_visited, nodes_visited):
        if int(nodes_visited, 2) == (pow(2, len(self.nodes)) - 1):
            return 0

        nbours = graph[node]
        nodes_visited = int(nodes_visited, 2) | (1 << node)
        key_str = f"{nodes_visited:0{len(self.nodes)}b}"

        if node not in self.memo:
            self.memo[node] = {}

        if key_str in self.memo[node]:
            return self.memo[node][key_str]

        ret_val = self.max_len
        for nb in nbours:
            path = str(node) + "-" + str(nb)
            rec_result = None
            if path in path_visited:
                continue

            path_visited.add(path)
            rec_result = self.dfs(nb, graph, path_visited, key_str)
            path_visited.remove(path)

            ret_val = min(ret_val, (rec_result + 1))

        if ret_val != self.max_len:
            self.memo[node][key_str] = ret_val
        return ret_val

    def shortest_path_bfs(self, graph):
        lst = []
        nodes_visited = f"{0:0{len(graph)}b}"
        for nd in range(len(graph)):
            lst.append((nd, nodes_visited, 0))

        memo = {}

        while lst:
            item = lst.pop(0)

            nd = item[0]
            nodes_visited_now = int(item[1], 2) | (1 << nd)

            if nodes_visited_now == (pow(2, len(graph)) - 1):
                return item[2]

            nodes_visited_now_as_str = f"{nodes_visited_now:0{len(graph)}b}"

            if nd not in memo:
                memo[nd] = set()

            if nodes_visited_now_as_str in memo[nd]:
                continue

            memo[nd].add(nodes_visited_now_as_str)

            for nb in graph[nd]:
                lst.append((nb, nodes_visited_now_as_str, item[2] + 1))

        return -1
