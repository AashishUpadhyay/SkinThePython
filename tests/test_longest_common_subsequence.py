from src.longest_common_subsequence import LongestCommonSubsequence

def test1():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('ghbrgc', 'hcbgcrbh')
    exp = 4
    assert rec == exp

def test2():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('ace', 'abcde')
    exp = 3
    assert rec == exp

def test3():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('abc', 'abc')
    exp = 3
    assert rec == exp

def test4():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('abc', 'def')
    exp = 0
    assert rec == exp


def test5():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('pmjghexybyrgzczy', 'hafcdqbgncrcbihkd')
    exp = 4
    assert rec == exp

def test6():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('jghexybyrgzcz', 'fcdqbgncrcbih')
    exp = 3
    assert rec == exp

def test7():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('psnw', 'vozsh')
    exp = 1
    assert rec == exp

def test8():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('ghbrzcz', 'fcbgrbh')
    exp = 2
    assert rec == exp

def test9():
    lcs = LongestCommonSubsequence()
    rec = lcs.find('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    exp = 210
    assert rec == exp
