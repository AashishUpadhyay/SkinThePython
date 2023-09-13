class Permutations:
    def __init__(self, arr):
        self._arr = arr
        self._perms = []

    def generatePermutations(self):
        self._generatePermutationsInternal(self._arr, "", set())
        return self._perms

    def _generatePermutationsInternal(self, arr, perm, seen):
        if len(arr) == len(seen):
            self._perms.append(perm)

        for i in range(len(arr)):
            if i in seen:
                continue

            seen.add(i)
            self._generatePermutationsInternal(arr, perm + arr[i], seen)
            seen.remove(i)
