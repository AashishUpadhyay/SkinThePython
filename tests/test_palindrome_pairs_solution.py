from src.palindrome_pairs_solution import PalindromePairsSolution


def test_1():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(
        [
            "abcd",
            "dcba",
            "lls",
            "s",
            "sssll",
        ]
    )
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[0, 1], [1, 0], [3, 2], [2, 4]])
    assert rcvd_sorted == exected


def test_2():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(["bat", "tab", "cat"])
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[0, 1], [1, 0]])
    assert rcvd_sorted == exected


def test_3():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(["a", ""])
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[0, 1], [1, 0]])
    assert rcvd_sorted == exected


def test_4():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(["eef", "f", "edc", "fede"])
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[1, 0], [3, 1]])
    assert rcvd_sorted == exected


def test_5():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(
        [
            "efedc",
            "c",
            "eef",
            "f",
            "edc",
            "acd",
            "fdc",
            "cffef",
            "fede",
            "efb",
            "bfbfd",
            "bd",
            "efccee",
            "ebaead",
            "fb",
            "bfbdd",
            "bbb",
            "cffaefd",
            "cbe",
            "febaedeb",
        ]
    )
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[3, 2], [8, 3], [14, 3]])
    assert rcvd_sorted == exected


def test_6():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(["a", "b", "c", "ab", "ac", "aa"])
    rcvd_sorted = sorted(rcvd)
    exected = sorted([[3, 0], [1, 3], [4, 0], [2, 4], [5, 0], [0, 5]])
    assert rcvd_sorted == exected


def test_7():
    pps = PalindromePairsSolution()
    rcvd = pps.palindromePairs(
        [
            "efedc",
            "c",
            "eef",
            "f",
            "edc",
            "acd",
            "fdc",
            "cffef",
            "fede",
            "efb",
            "bfbfd",
            "bd",
            "efccee",
            "ebaead",
            "fb",
            "bfbdd",
            "bbb",
            "cffaefd",
            "cbe",
            "febaedeb",
            "eaded",
            "aaafa",
            "ba",
            "bcfdcfec",
            "acbcbfb",
            "cbbb",
            "cf",
            "ecd",
            "deafdbb",
            "feebbbf",
            "dfed",
            "baafc",
            "fdf",
            "e",
            "defdf",
            "dccfddd",
            "bb",
            "facaabee",
            "ffe",
            "adecbe",
            "dbcacfba",
            "a",
            "edceaa",
            "be",
            "bea",
            "eaddc",
            "dd",
            "fcccaeb",
            "b",
            "fbe",
            "fffb",
            "bffbb",
            "ebbac",
            "fa",
            "bcdbced",
            "bcdeac",
            "bdeca",
            "aeeeea",
            "d",
            "ceb",
            "addcfab",
            "ccfccfa",
            "ebddbac",
            "abbcddba",
            "caebebee",
            "bf",
            "dacbcdd",
            "aedccd",
            "fadcaa",
            "adda",
            "da",
            "dfebae",
            "cdb",
            "db",
            "fde",
            "fcbecf",
            "efbdbcac",
            "aaba",
            "befcfefa",
            "eafdadad",
            "ebdadcb",
            "ebddc",
            "deb",
            "aaed",
            "edca",
            "cd",
            "cbecfdfb",
            "aecd",
            "beaedbcd",
            "ad",
            "ecabdb",
            "caddbaf",
            "aaad",
            "ddf",
            "badfed",
            "df",
            "eadbccad",
            "fedcee",
            "bbfaafbf",
            "cb",
            "af",
            "eb",
            "beecd",
            "ebfda",
            "bdba",
            "aa",
            "dcba",
            "ddcea",
            "ca",
            "cda",
            "fe",
        ]
    )
    rcvd_sorted = sorted(rcvd)
    exected = sorted(
        [
            [85, 0],
            [110, 2],
            [3, 2],
            [85, 4],
            [5, 108],
            [85, 6],
            [6, 95],
            [8, 3],
            [65, 9],
            [9, 110],
            [95, 10],
            [11, 48],
            [58, 11],
            [11, 73],
            [14, 3],
            [48, 14],
            [14, 65],
            [46, 15],
            [16, 48],
            [36, 16],
            [16, 36],
            [48, 16],
            [101, 18],
            [21, 105],
            [100, 21],
            [22, 48],
            [41, 22],
            [25, 1],
            [16, 25],
            [26, 1],
            [3, 26],
            [32, 95],
            [34, 30],
            [36, 48],
            [48, 36],
            [33, 38],
            [43, 48],
            [33, 43],
            [43, 101],
            [44, 101],
            [46, 58],
            [58, 46],
            [101, 49],
            [49, 65],
            [65, 50],
            [48, 50],
            [48, 51],
            [53, 3],
            [41, 53],
            [53, 100],
            [43, 59],
            [100, 61],
            [65, 48],
            [3, 65],
            [65, 14],
            [70, 58],
            [41, 70],
            [70, 89],
            [11, 72],
            [73, 58],
            [48, 73],
            [73, 11],
            [74, 95],
            [77, 41],
            [43, 82],
            [5, 84],
            [85, 1],
            [58, 85],
            [89, 41],
            [58, 89],
            [89, 70],
            [70, 92],
            [58, 92],
            [93, 46],
            [3, 93],
            [95, 58],
            [3, 95],
            [99, 1],
            [48, 99],
            [100, 41],
            [3, 100],
            [100, 53],
            [101, 33],
            [48, 101],
            [101, 43],
            [41, 104],
            [105, 41],
            [41, 105],
            [87, 107],
            [108, 1],
            [41, 108],
            [89, 109],
            [110, 3],
            [33, 110],
        ]
    )
    assert rcvd_sorted == exected
