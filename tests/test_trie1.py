from src.datastructures.trie1 import Trie


def test1():
    trie = Trie()
    trie.add("i love you")
    trie.add("i love leetcode")
    trie.add("ironman")
    trie.add("island")
    trie.add("i a")

    res = trie.find("i")
    res_set = set(res)
    assert "i love you" in res_set
    assert "i love leetcode" in res_set
    assert "ironman" in res_set
    assert "island" in res_set
    assert "i a" in res_set
    assert len(res) == 5

    res = trie.find("i ")
    res_set = set(res)
    assert "i love you" in res_set
    assert "i love leetcode" in res_set
    assert "i a" in res_set
    assert len(res) == 3

    res = trie.find("ironman")
    res_set = set(res)
    assert "ironman" in res_set
    assert len(res) == 1

    res = trie.find("island")
    res_set = set(res)
    assert "island" in res_set
    assert len(res) == 1

    res = trie.find("as")
    assert len(trie.find("as")) == 0
