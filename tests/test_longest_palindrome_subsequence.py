from src.longest_palindrome_subsequence import LongestPalindromeSubsequence


def test1():
    lps = LongestPalindromeSubsequence()
    assert lps.find("agbdba") == 5


def test2():
    lps = LongestPalindromeSubsequence()
    assert lps.find("agbddba") == 6


def test3():
    lps = LongestPalindromeSubsequence()
    assert lps.find("bbbab") == 4


def test4():
    lps = LongestPalindromeSubsequence()
    assert lps.find("a") == 1
