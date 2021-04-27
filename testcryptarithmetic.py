from src.cryptarithmetic import Cryptarithmetic
from collections import OrderedDict
import sys


def testisvalid1():
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    # words = ['9567','1O85', '1O652']

    wordsArr = []
    letters = {}

    for w in words:
        for c in w:
            if c not in letters:
                letters[c] = None

    letters["S"] = None
    letters["E"] = None
    letters["N"] = None
    letters["D"] = 7
    letters["M"] = None
    letters["O"] = None
    letters["R"] = None
    letters["Y"] = None
    letters["#"] = 0

    for w in words:
        wordArr = []
        for c in w:
            wordArr.append(c)
        wordsArr.append(wordArr)

    crypt.normalizeWords(wordsArr)
    assert True == crypt.isValid(wordsArr, letters)


def testisvalid2():
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    # words = ['9567','1O85', '1O652']

    wordsArr = []
    letters = {}

    for w in words:
        for c in w:
            if c not in letters:
                letters[c] = None

    letters["S"] = None
    letters["E"] = 5
    letters["N"] = None
    letters["D"] = 7
    letters["M"] = None
    letters["O"] = None
    letters["R"] = None
    letters["Y"] = None
    letters["#"] = 0

    for w in words:
        wordArr = []
        for c in w:
            wordArr.append(c)
        wordsArr.append(wordArr)

    crypt.normalizeWords(wordsArr)
    assert True == crypt.isValid(wordsArr, letters)


def testisvalid3():
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    # words = ['9567','1O85', '1O652']

    wordsArr = []
    letters = {}

    for w in words:
        for c in w:
            if c not in letters:
                letters[c] = None

    letters["S"] = None
    letters["E"] = 5
    letters["N"] = None
    letters["D"] = 7
    letters["M"] = None
    letters["O"] = None
    letters["R"] = None
    letters["Y"] = 2
    letters["#"] = 0

    for w in words:
        wordArr = []
        for c in w:
            wordArr.append(c)
        wordsArr.append(wordArr)

    crypt.normalizeWords(wordsArr)
    assert True == crypt.isValid(wordsArr, letters)


def testisvalid4():
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    # words = ['9567','1O85', '1O652']

    wordsArr = []
    letters = {}

    for w in words:
        for c in w:
            if c not in letters:
                letters[c] = None

    letters["S"] = None
    letters["E"] = 5
    letters["N"] = None
    letters["D"] = 7
    letters["M"] = None
    letters["O"] = None
    letters["R"] = None
    letters["Y"] = 3
    letters["#"] = 0

    for w in words:
        wordArr = []
        for c in w:
            wordArr.append(c)
        wordsArr.append(wordArr)

    crypt.normalizeWords(wordsArr)
    assert False == crypt.isValid(wordsArr, letters)


def testisvalid5():
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    # words = ['9567','1O85', '1O652']

    wordsArr = []
    letters = {}

    for w in words:
        for c in w:
            if c not in letters:
                letters[c] = None

    letters["S"] = 9
    letters["E"] = 5
    letters["N"] = 6
    letters["D"] = 7
    letters["M"] = 1
    letters["O"] = 0
    letters["R"] = 8
    letters["Y"] = 2
    letters["#"] = 0

    for w in words:
        wordArr = []
        for c in w:
            wordArr.append(c)
        wordsArr.append(wordArr)

    crypt.normalizeWords(wordsArr)
    assert True == crypt.isValid(wordsArr, letters)


def testNormalizeWords():
    crypt = Cryptarithmetic([])
    words = [["S", "E", "N", "D"], ["M", "O", "R", "E"], ["M", "O", "N", "E", "Y"]]
    crypt.normalizeWords(words)
    assert words[0][0] == "#"
    assert words[1][0] == "#"


def test1():
    words = ["B", "AC", "AD"]
    crypt = Cryptarithmetic(words)
    result = crypt.solve()
    found = False
    for r in result:
        if r["B"] == 8 and r["C"] == 1 and r["D"] == 9 and r["A"] == 7:
            found = True
            break

    assert found


def test2():
    sys.setrecursionlimit(1500)
    words = ["SEND", "MORE", "MONEY"]
    crypt = Cryptarithmetic(words)
    result = crypt.solve()
    found = False
    for r in result:
        if (
            r["D"] == 7
            and r["E"] == 5
            and r["Y"] == 2
            and r["N"] == 6
            and r["R"] == 8
            and r["O"] == 0
            and r["S"] == 9
            and r["M"] == 1
        ):
            found = True

    assert found


def testisvalid6():
    letters = OrderedDict(
        [
            ("S", 0),
            ("E", 1),
            ("N", 2),
            ("D", None),
            ("M", None),
            ("O", None),
            ("R", None),
            ("Y", None),
        ]
    )

    wordsArr = [
        ["#", "S", "E", "N", "D"],
        ["#", "M", "O", "R", "E"],
        ["M", "O", "N", "E", "Y"],
    ]
    crypt = Cryptarithmetic([])
    crypt.normalizeWords(wordsArr)
    letters = {}
    maxLen = len(wordsArr[2])

    for i in range(maxLen - 1, -1, -1):
        for w in wordsArr:
            if w[i] not in letters:
                letters[w[i]] = None

    letters["D"] = 0
    letters["E"] = 1
    letters["Y"] = 2

    assert False == crypt.isValid(wordsArr, letters)


def testisvalid7():
    letters = OrderedDict(
        [
            ("S", 0),
            ("E", 1),
            ("N", 2),
            ("D", None),
            ("M", None),
            ("O", None),
            ("R", None),
            ("Y", None),
        ]
    )

    wordsArr = [
        ["#", "S", "E", "N", "D"],
        ["#", "M", "O", "R", "E"],
        ["M", "O", "N", "E", "Y"],
    ]
    crypt = Cryptarithmetic([])
    crypt.normalizeWords(wordsArr)
    letters = {}
    maxLen = len(wordsArr[2])

    for i in range(maxLen - 1, -1, -1):
        for w in wordsArr:
            if w[i] not in letters:
                letters[w[i]] = None

    letters["D"] = 1
    letters["E"] = 2
    letters["Y"] = 3

    assert True == crypt.isValid(wordsArr, letters)
