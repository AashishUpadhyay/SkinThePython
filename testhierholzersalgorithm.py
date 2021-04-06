from hierholzersalgorithm import debrujin_sequence, _build_vertices, _build_debrujin_sequence, _build_graph, _build_vertices

def test_find_matches1():
    vertices = _build_vertices(['0', '1', '2'],3)
    debrujin_seq = debrujin_sequence(['0', '1', '2'],3)
    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test_find_matches2():
    vertices = _build_vertices(['0', '1', '2'],2)
    debrujin_seq = debrujin_sequence(['0', '1', '2'],2)
    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test_find_matches3():
    vertices = _build_vertices(['0'],1)
    debrujin_seq = debrujin_sequence(['0'],1)

    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test_find_matches4():
    arr = ['0','1', '2','3']
    vertices = _build_vertices(arr,3)
    debrujin_seq = debrujin_sequence(arr,3)
    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test_find_matches5():
    arr = ['0','1']
    vertices = _build_vertices(arr,1)
    debrujin_seq = debrujin_sequence(arr,1)

    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test__build_debrujin_sequence():
    graph = {
        '000':['000', '001'],
        '001':['010', '011'],
        '010':['100', '101'],
        '011':['110', '111'],
        '100':['000', '001'],
        '101':['010', '011'],
        '110':['101', '100'],
        '111':['110', '111'],
        }

    vertices = _build_vertices(['0', '1'],4)
    seq = _build_debrujin_sequence(graph, 3,'0')
    debrujin_seq = "".join(seq)
     
    print(debrujin_seq) 
    for v in vertices:
        if debrujin_seq.count(v) != 1:
            assert False

def test_find_matches6():
    arr = ['0','1']
    vertices = _build_vertices(arr,4)
    debrujin_seq = debrujin_sequence(arr,4)
    print(debrujin_seq)
    for v in vertices:
        print(v)
        if debrujin_seq.count(v) != 1:
            assert False

def test_build_vertices():
    vertices = _build_vertices(['0','1','2'],1)
    assert 3 == len(vertices)

def test_build_graph():
    graph = _build_graph(['0','1','2'],1)
    assert '0' in graph
    assert '1' in graph
    assert '2' in graph
    assert set(['0','1','2']) == set(graph['0'])
    assert set(['0','1','2']) == set(graph['1'])
    assert set(['0','1','2']) == set(graph['2'])

def test_build_graph1():
    graph = _build_graph(['0','1'],1)
    
    assert '0' in graph
    assert '1' in graph
    assert set(['0','1']) == set(graph['0'])
    assert set(['0','1']) == set(graph['1'])

def test_build_graph2():
    graph = _build_graph(['0','1'],3)
    
    assert set(graph['000']) == set(['000', '001'])
    assert set(graph['001']) == set(['010', '011'])
    assert set(graph['010']) == set(['100', '101'])
    assert set(graph['011']) == set(['110', '111'])
    assert set(graph['101']) == set(['010', '011'])
    assert set(graph['110']) == set(['101', '100'])
    assert set(graph['111']) == set(['110', '111'])



