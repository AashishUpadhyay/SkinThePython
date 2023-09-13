import collections


class LongestRepeatingSubstring:
    def __init__(self) -> None:
        pass

    def find(self, s):
        L = (len(s) + 1) // 2
        rv = 0
        mod = (1 << 20) - 1

        while L > rv:
            if self.search(L, s, mod):
                rv = max(rv, L)
                L += 1
            else:
                L -= 1
        return rv

    def search(self, L, s, mod):
        N = len(s)
        hsh = 0
        for i in range(L):
            hsh = (hsh * 26 + self.val(s[i])) % mod

        seen = set()
        seen.add(hsh)
        aL = pow(26, L - 1, mod)

        for i in range(L, N):
            in_c = self.val(s[i])
            out_c = self.val(s[i - L])
            hsh = ((hsh - (out_c * aL)) * 26 + in_c) % mod
            if hsh in seen:
                return True
            seen.add(hsh)
        return False

    def val(self, c):
        return ord(c) - 97

    def findstring(self, s):
        rv = [-1, -1]
        mod = (1 << 64) - 1
        ml = 0
        s_to_num = [self.val(c) for c in s]

        N = len(s)
        si = 0
        ei = N - 1
        L = 0

        while si <= ei:
            mid = si + (ei - si) // 2
            L = ml + (mid - si + 1)
            rng = self.searchstring(L, s, mod, s_to_num)
            if rng:
                ml = max(ml, rng[1] - rng[0])
                si = mid + 1
                rv = rng
            else:
                ei = mid - 1
        return s[rv[0] : rv[1]]

    def searchstring(self, L, s, mod, s_to_num):
        N = len(s)
        hsh = 0
        for i in range(L):
            hsh = (hsh * 26 + self.val(s[i])) % mod

        seen = collections.defaultdict(list)
        seen[hsh] = [0]
        aL = pow(26, L - 1, mod)

        for i in range(L, N):
            in_c = self.val(s[i])
            out_c = self.val(s[i - L])
            hsh = ((hsh - (out_c * aL)) * 26 + in_c) % mod
            if hsh in seen:
                curr_lst = s_to_num[i - L + 1 : i + 1]
                all_others = [s_to_num[idx : idx + L] for idx in seen[hsh]]
                if any(curr_lst == item for item in all_others):
                    return [i - L + 1, i + 1]
            seen[hsh].append(i - L + 1)
        return []

    def val(self, c):
        return ord(c) - 97
