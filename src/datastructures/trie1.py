class Trie:

    def __init__(self):
        self.children = {}
        self.data = None

    def add(self, word):
        trie = self
        for c in word:
            if c not in trie.children:
                trie.children[c] = Trie()
            trie = trie.children[c]

        if '#' not in trie.children:
            trie.children['#'] = None

        trie.data = word

    def find(self, word):
        trie = self.find_internal(word)

        if not trie:
            return []

        return self.dfs(trie)

    def find_internal(self, word):
        trie = self

        for c in word:
            if c not in trie.children:
                return None
            trie = trie.children[c]

        return trie

    def dfs(self, node):

        result = []
        if node:
            if '#' in node.children:
                result.append(node.data)

            for k in node.children.keys():
                items = self.dfs(node.children[k])
                result.extend(items)
        return result
