class LongestRepeatingSubstring:
    def __init__(self) -> None:
        pass

    def find(self, s):
        L = (len(s) + 1)//2
        rv = 0
        mod = (1 << 64)-1

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
        h = 0
        for i in range(L):
            hsh = (hsh*26 + self.val(s[i])) % mod

        seen = set()
        seen.add(hsh)
        aL = pow(26, L-1, mod)

        for i in range(L, N):
            in_c = self.val(s[i])
            out_c = self.val(s[i-L])
            hsh = ((hsh - (out_c*aL)) * 26 + in_c) % mod
            if hsh in seen:
                return True
            seen.add(hsh)
        return False

    def val(self, c):
        return ord(c)-97
