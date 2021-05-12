from src.datastructures.trie import Trie


class Ghost:
    def findWinningLetters(self, words):
        result = []
        d = Trie(words)

        ks = d.trie.keys()
        for k in ks:
            if self.isWinning(k, d):
                result.append(k)

        return result

    def isWinning(self, prefix, trie):
        d = trie.find(prefix)

        if "#" in d:
            return False
        else:
            ks = d.keys()
            for k in ks:
                if self.isWinning(prefix + k, trie) == False:
                    return True

            return False
