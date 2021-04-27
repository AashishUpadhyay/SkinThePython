def debrujin_sequence(arr: [], k: int) -> str:
    if k < 1 or len(arr) == 0:
        raise Exception()

    if k == 1:
        return "".join(arr)

    graph = _build_graph(arr, k - 1)
    seq = _build_debrujin_sequence(graph, k - 1, arr[0])

    return "".join(seq)


def _build_debrujin_sequence(graph: {}, node_char_count, start_char):
    start_node = start_char * (node_char_count)
    seq = []
    visited = set([])
    _dfs(graph, start_node, node_char_count, seq, visited)
    seq.append(start_node[0:-1])
    return seq


def _dfs(graph: {}, node, node_char_count, seq, visited):
    vals = graph[node]
    for v in vals:
        edge = (node + v[1:]) if node_char_count > 1 else (node + v)
        if edge not in visited:
            visited.add(edge)
            _dfs(graph, v, node_char_count, seq, visited)
    seq.append(node[-1])


def _build_graph(arr: [], node_char_count: int):
    vertices = _build_vertices(arr, node_char_count, 0)

    graph = {}
    for v in vertices:
        graph[v] = []
        for c in arr:
            graph[v].append(v[1:] + c)

    return graph


def _build_vertices(arr: [], node_char_count: int, cnt_index: int = 0):
    result = []

    if cnt_index >= node_char_count:
        return result

    for i in arr:
        returned_val = _build_vertices(arr, node_char_count, cnt_index + 1)

        if len(returned_val):
            result.extend([i + val for val in returned_val])
        else:
            result.append(i)

    return result
