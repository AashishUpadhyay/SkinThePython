from src.aliendictionary import AlienDictionary


def testbuildgraph1():
    words = ["abc", "bcd", "bcdr"]
    ad = AlienDictionary(words)

    assert len(ad._graph["a"]) == 1
    assert len(ad._graph["b"]) == 0
    assert len(ad._graph["c"]) == 0
    assert len(ad._graph["d"]) == 0
    assert len(ad._graph["r"]) == 0


def testbuildgraph2():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    ad = AlienDictionary(words)

    assert len(ad._graph["t"]) == 1
    assert len(ad._graph["w"]) == 1
    assert len(ad._graph["r"]) == 1
    assert len(ad._graph["e"]) == 1
    assert len(ad._graph["f"]) == 0


def testbuildgraph3():
    words = ["x", "z", "x"]
    ad = AlienDictionary(words)

    assert len(ad._graph["x"]) == 1
    assert len(ad._graph["z"]) == 1


def testbuildreversegraph():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    ad = AlienDictionary(words)
    rev = ad._buildReverseGraph(ad._graph)

    assert len(rev["e"]) == 1
    assert len(rev["t"]) == 1
    assert len(rev["f"]) == 1
    assert len(rev["r"]) == 1
    assert "w" not in rev


def testfindorder1():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    ad = AlienDictionary(words)
    assert "wertf" == ad.findOrder()


def testfindorder2():
    words = ["z", "x"]
    ad = AlienDictionary(words)
    assert "zx" == ad.findOrder()


def testfindorder3():
    words = ["z", "x", "z"]
    ad = AlienDictionary(words)
    assert "" == ad.findOrder()


def testfindorder4():
    words = ["za", "zb", "ca", "cb"]
    ad = AlienDictionary(words)
    order = ad.findOrder()
    assert "abzc" == order or "zacb" == order


def testfindorder5():
    words = ["z", "z"]
    ad = AlienDictionary(words)
    order = ad.findOrder()
    assert "z" == order


def testfindorder6():
    words = ["qjatu", "ekp", "daysdbi", "ntbjwvta"]
    ad = AlienDictionary(words)
    order = ad.findOrder()

    assert "abijkpqednstuvwy" == order or order == "qedvwnibsypkutaj"


def testfindorder7():
    words = ["bsusz", "rhn", "gfbrwec", "kuw", "qvpxbexnhx", "gnp", "laxutz", "qzxccww"]
    ad = AlienDictionary(words)
    order = ad.findOrder()
    assert "" == order


def testfindorder8():
    words = ["abc", "ab"]
    ad = AlienDictionary(words)
    order = ad.findOrder()
    assert "" == order
