from src.longestrepeatingsubstring import LongestRepeatingSubstring


def test1():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('aashish') == 2


def test2():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('leetcodecodeleet') == 4


def test3():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('aaaaaaa') == 6


def test4():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('asdf') == 0


def test5():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('abbaba') == 2


def test6():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('aabcaabdaab') == 3


def test7():
    lrs = LongestRepeatingSubstring()
    assert lrs.find('aaaaa') == 4


def test8():
    lrs = LongestRepeatingSubstring()
    assert lrs.find(
        'aaabaabbbaaabaabbaabbbabbbaaaabbaaaaaabbbaabbbbbbbbbaaaabbabbabaaaabaabbbaaabaabbaabbbabbbaaaabbaaaaaabbbaabbbbbbbbbaaaabbabbaba') == 64


def test9():
    lrs = LongestRepeatingSubstring()
    assert lrs.find(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 999
