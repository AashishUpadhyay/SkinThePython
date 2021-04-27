import copy
from collections import OrderedDict


class Cryptarithmetic:
    def __init__(self, problem):
        self.words = problem
        self.result = []

    def solve(self):
        wordsArr = []
        for w in self.words:
            wordArr = []
            for c in w:
                wordArr.append(c)
            wordsArr.append(wordArr)

        self.normalizeWords(wordsArr)

        letters = OrderedDict()
        maxLen = len(self.words[2])

        for i in range(maxLen - 1, -1, -1):
            for w in wordsArr:
                if w[i] not in letters:
                    letters[w[i]] = None

        unassigned = [key for key in letters.keys() if key != "#"]
        letters["#"] = 0
        self.solveInternal(letters, unassigned, wordsArr, set())
        return self.result

    def solveInternal(self, letters, unassigned, wordsArr, seen):
        if not unassigned:
            if self.isValid(wordsArr, letters):
                self.result.append(copy.deepcopy(letters))
            return

        c = unassigned[0]
        for i in range(10):
            if i in seen:
                continue

            letters[c] = i
            seen.add(i)

            if self.isValid(wordsArr, letters):
                self.solveInternal(letters, unassigned[1:], wordsArr, seen)

            seen.remove(i)
            letters[c] = None

        return None

    def isValid(self, wordsArr, letters):
        a, b, c = wordsArr
        n = len(wordsArr[0])
        carry = 0
        for i in range(n - 1, -1, -1):
            if any(letters[w[i]] == None for w in wordsArr if w[i] != "#"):
                return True
            elif (letters[a[i]] + letters[b[i]] + carry) == letters[c[i]]:
                carry = 0
            elif (letters[a[i]] + letters[b[i]] + carry) == (10 + letters[c[i]]):
                carry = 1
            else:
                return False

        return True

    def normalizeWords(self, wordsArr):
        maxLen = len(wordsArr[2])

        for w in wordsArr:
            ct = maxLen - len(w)
            while ct > 0:
                w.insert(0, "#")
                ct = ct - 1
