class Trie:
    def __init__(self, words):
        self.trie = {}

        for w in words:
            self.insert(w)

    def insert(self, word):
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['#'] = None

    def find(self, word):
        d = self.trie

        for c in word:
            if c not in d:
                return None
            else:
                d = d[c]

        return d                                