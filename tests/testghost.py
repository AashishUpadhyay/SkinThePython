from src.ghost import Ghost


def test1():
    g = Ghost()
    assert set(["b", "c"]) == set(
        g.findWinningLetters(["cat", "calf", "bear", "dog", "ca"])
    )


def test2():
    g = Ghost()
    assert set(["c"]) == set(g.findWinningLetters(["ca"]))


def test3():
    g = Ghost()
    assert set(["b"]) == set(g.findWinningLetters(["bear"]))


def test4():
    g = Ghost()
    assert set([]) == set(g.findWinningLetters(["bear", "bea"]))
