from src.cheapestitinerary import CheapestItinerary


def testbuildGraph():
    routes = [
        ("JFK", "ATL", 150),
        ("ATL", "SFO", 400),
        ("ORD", "LAX", 500),
        ("LAX", "DFW", 80),
        ("JFK", "HKG", 800),
        ("ATL", "ORD", 90),
        ("JFK", "LAX", 500),
    ]
    ci = CheapestItinerary(routes)

    graph = ci._buildGraph(routes)

    assert len(graph["JFK"]) == 3
    assert len(graph["ATL"]) == 2
    assert len(graph["LAX"]) == 1
    assert len(graph["ORD"]) == 1
    assert "HKG" not in graph
    assert "DFW" not in graph


def testfindCheapestPrice1():
    routes = [
        ("JFK", "ATL", 150),
        ("ATL", "SFO", 400),
        ("ORD", "LAX", 200),
        ("LAX", "DFW", 80),
        ("JFK", "HKG", 800),
        ("ATL", "ORD", 90),
        ("JFK", "LAX", 500),
    ]
    ci = CheapestItinerary(routes)
    assert 440 == ci.findCheapestPrice("JFK", "LAX", 3)


def testfindCheapestPrice2():
    routes = [
        ("JFK", "ATL", 150),
        ("ATL", "SFO", 400),
        ("ORD", "LAX", 200),
        ("LAX", "DFW", 80),
        ("JFK", "HKG", 800),
        ("ATL", "ORD", 90),
        ("JFK", "LAX", 500),
    ]
    ci = CheapestItinerary(routes)
    assert 500 == ci.findCheapestPrice("JFK", "LAX", 2)
