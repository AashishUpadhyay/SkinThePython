
from src.rabinkarp import find_matches, find_matches_rabinkarp


def test_find_matches1():

    assert find_matches("abracadabra", "abr") == find_matches_rabinkarp(
        "abracadabra", "abr")


def test_find_matches2():

    assert find_matches("aaaabbbaaaaa", "aaa") == find_matches_rabinkarp(
        "aaaabbbaaaaa", "aaa")


def test_find_matches3():

    assert find_matches("aaabrabbbaabraaa", "abr") == find_matches_rabinkarp(
        "aaabrabbbaabraaa", "abr")
