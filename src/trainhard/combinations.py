from functools import cache


class Solution:
    def generate_combinations(self, items, r):
        """
        Generate all possible combinations of r items from the input list.

        Args:
            items: List of items to generate combinations from
            r: Number of items to include in each combination

        Returns:
            List of tuples, where each tuple is a combination of r items
        """
        rv = []
        n = len(items)

        @cache
        def bt(si, r, visited):
            if r == 0:
                rv.append(translate(visited))
                return

            for idx in range(si+1, n):
                bt(idx, r-1, visited | (1 << idx))

        def translate(val):
            grp = []
            for i in range(0, len(items)):
                if val & (1 << i):
                    grp.append(items[i])
            return grp

        for i in range(0, len(items)-r+1):
            bt(i, r-1, 1 << i)
        return rv
