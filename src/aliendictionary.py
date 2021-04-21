class AlienDictionary:
    def __init__(self, words):
        self._graph = self._buildGraph(words)
        self._revgraph = self._buildReverseGraph(self._graph)

    def _buildGraph(self, words):
        graph = {}

        for ch in words[0]:   
            if ch not in graph:
                graph[ch] = set() 

        for i in range(1, len(words)):
            c = 0

            # for chutiya test case by leetcode
            if len(words[i-1]) > len(words[i]) and words[i-1].startswith(words[i]):
                return {}

            while c < len(words[i-1]) and c < len(words[i]) and words[i-1][c] == words[i][c]:
                if words[i-1][c] not in graph:
                    graph[words[i-1][c]] = set()
                c+=1

            if c < len(words[i-1]) and c < len(words[i]):
                graph[words[i-1][c]].add(words[i][c])

            while c < len(words[i]):   
                if words[i][c] not in graph:
                    graph[words[i][c]] = set()  
                c+=1 

        return graph

    def _buildReverseGraph(self, graph):
        revgraph = {}

        for k, vals in graph.items():
            for v in vals:
                if v not in revgraph:
                    revgraph[v] = []

                revgraph[v].append(k)    

        return revgraph

    def findOrder(self):
        
        source = [k for k,v in self._graph.items() if len(v) == 0]
        target = []

        while source:
            popped = source.pop(0)
            target.append(popped)

            if popped in self._revgraph:
                graphKeys = self._revgraph[popped]

                for key in graphKeys:
                    self._graph[key].remove(popped)

                    if len(self._graph[key]) == 0:
                        source.append(key)

        if len(target) < len(self._graph):
            return ""

        return "".join(list(reversed(target)))
