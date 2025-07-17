from typing import List, Dict, Set
from collections import defaultdict
from functools import cache


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        rv = 1
        graph = defaultdict(list)

        for _, edge in enumerate(edges):
            nd1, nd2 = edge
            if nd1 not in graph:
                graph[nd1] = []
            if nd2 not in graph:
                graph[nd2] = []
            graph[nd1].append(nd2)
            graph[nd2].append(nd1)

        @cache
        def dfs(nd1, nd2, seen):
            if nd2 < nd1:
                return dfs(nd2, nd1, seen)
            # print(f"nd1: {nd1}, nd2: {nd2}, seen: {seen}")
            if label[nd1] != label[nd2]:
                return 0

            rv = 0
            if nd1 == nd2:
                newlen = 1
            else:
                newlen = 2

            nd1_nbours = graph[nd1]
            nd2_nbours = graph[nd2]

            for nd1_nbour in nd1_nbours:
                if (1 << nd1_nbour) & seen:
                    continue
                for nd2_nbour in nd2_nbours:
                    if (1 << nd2_nbour) & seen:
                        continue
                    if (nd1_nbour == nd2_nbour):
                        if (nd1 != nd2):
                            # common neighbour for two nodes, recursion ends here
                            rv = max(rv, newlen)
                    else:
                        dfs_val = dfs(nd1_nbour, nd2_nbour, seen |
                                      1 << nd1_nbour | 1 << nd2_nbour)
                        rv = max(rv, newlen + dfs_val)
                    # print(
                    #    f"nd1: {nd1}, nd2: {nd2}, nd1_nbour: {nd1_nbour}, nd2_nbour: {nd2_nbour}, rv: {rv}, seen:{seen}")
            return max(rv, newlen)
        visited = set()
        for nd1 in range(n):
            # Check single node paths
            rv = max(rv, dfs(nd1, nd1, 1 << nd1))

            visited.add(nd1)
            # Check unvisited neighbors for palindromic paths
            for nd2 in graph[nd1]:
                if nd2 in visited:  # Skip if we've already processed this pair
                    continue
                rv = max(rv, dfs(nd1, nd2, 1 << nd1 | 1 << nd2))

        return rv
