class LongestPalindromeSubsequence:
    def __init__(self) -> None:
        pass

    def find(self, s):
        N = len(s)

        dp = [[1 if aj == ai else 0 for aj in range(N)] for ai in range(N)]
        rv = 1
        for l in range(2, N+1):
            for i in range(0, N):
                si = i
                ei = min(si+l-1, N-1)

                if (ei-si+1) < l:
                    continue
                
                if s[si] == s[ei]:
                    dp[si][ei] = dp[si+1][ei-1] + 2
                else:
                    dp[si][ei] = max(dp[si+1][ei], dp[si][ei-1])
                rv = max(rv, dp[si][ei])
        return rv

        
