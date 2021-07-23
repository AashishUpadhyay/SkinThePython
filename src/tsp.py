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
            nodes_visited = set()
            result = min(self.dfs(k, adj_list, path_visited, nodes_visited), result)

        return result - 1 
    
    def dfs(self, node, graph, path_visited, nodes_visited):

        if len(nodes_visited) == len(self.nodes):
            return 0

        nbours = graph[node]

        key_arr = []
        key_arr.extend([str(ka) for ka in self.nodes if ka in nodes_visited]) 
        key_arr = [node]
        key_arr.extend([str(ka) for ka in self.nodes if ka not in nodes_visited ]) 
        key_str = "-".join([str(ka) for ka in key_arr])

        nodes_visited.add(node)
        
        if key_str in self.dp:
            return self.dp[key_str]

        ret_val = self.max_len
        for nb in nbours:
            path = str(node) + "-" + str(nb)
            rec_result = None
            if path not in path_visited:
                path_visited.add(path)
                graph[node].remove(nb)
                rec_result = self.dfs(nb, graph, path_visited, copy.deepcopy(nodes_visited))
                path_visited.remove(path)
                graph[node].add(nb)

                if rec_result == -1:
                    continue

            ret_val = min(ret_val, (rec_result+1))   
        
        self.dp[key_str] = ret_val
        return ret_val   

