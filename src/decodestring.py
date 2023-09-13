class DecodeString:
    def __init__(self) -> None:
        self.dp = {}

    def top_down(self, s):
        if len(s) == 0:
            return 1

        result = 0
        if s in self.dp:
            return self.dp[s]

        for j in range(1, min(len(s), 2) + 1):
            ss = s[0:j]

            if ss[0] == "0":
                break

            if int(ss) < 1 or int(ss) > 26:
                continue

            rv = self.top_down(s[len(ss) :])
            result += rv

        self.dp[s] = result
        return self.dp[s]

    def bottom_up(self, s):
        dp = [0 for i in range(len(s) + 1)]
        dp[len(dp) - 1] = 1

        for i in range(len(s) - 1, -1, -1):
            ss_1 = s[i]
            res = 0

            if not ss_1[0] == "0":
                if int(ss_1) > 0 and int(ss_1) < 27:
                    res += dp[i + 1]

                if i < len(s) - 1:
                    ss_2 = s[i : i + 2]
                    if int(ss_2) > 0 and int(ss_2) < 27:
                        res += dp[i + 2]

            dp[i] = res

        return dp[0]
