class DecodeString:
    def __init__(self) -> None:
        self.dp ={}

    def top_down(self, s):
        if len(s) == 0:
            return 1

        result = 0
        if s in self.dp:
            return self.dp[s]

        for j in range(1, min(len(s), 2)+1):
            ss = s[0:j]

            if ss[0] == '0':
                break

            if int(ss) < 1 or int(ss) > 26:
                continue

            rv = self.top_down(s[len(ss):])
            result += rv
                
        self.dp[s] = result        
        return self.dp[s]      



