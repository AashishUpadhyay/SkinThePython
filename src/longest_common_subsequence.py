class LongestCommonSubsequence:
    def __init__(self):
        pass

    def find(self, text1, text2):
        if len(text1) < len(text2):
            ss = text1
            ls = text2
        else:
            ss = text2
            ls = text1
        
        ls_map = self.t_map(ls)
        dp = {}
        result = 0
        for i, c in enumerate(ss):
            if i not in dp:
                dp[i] = []
            if self.is_sub(c, ls, ls_map):
                dp[i] = [1,[c]]
                result = 1
            else:
                dp[i] = [0,[]]
        for i in range(len(ss)):
            for j in range(0, i):

                sub_str = ss[j] + ss[i]
                if self.is_sub(sub_str, ls, ls_map):
                    l_sub_str = sub_str

                    if dp[i][0] < len(l_sub_str):
                        dp[i] = [len(l_sub_str), [l_sub_str]]
                        result = max(result, len(l_sub_str))
                    elif dp[i][0] == len(l_sub_str):
                        dp[i][1].append(l_sub_str)

                    sub_strs_at_j = dp[j][1]
                    for sub_str_at_j in sub_strs_at_j:
                        new_sub_str = sub_str_at_j + ss[i]

                        if self.is_sub(new_sub_str, ls, ls_map):
                            l_sub_str = new_sub_str

                            if dp[i][0] < len(l_sub_str):
                                dp[i] = [len(l_sub_str), [l_sub_str]]
                                result = max(result, len(l_sub_str))
                            elif dp[i][0] == len(l_sub_str):
                                dp[i][1].append(l_sub_str)
        return result

        
    def is_sub(self, s, t, t_char_ind_map):
        lmi = -1
        cnt = 0
        for sc in s:
            if sc not in t_char_ind_map:
                return False
            indices = sorted(t_char_ind_map[sc])
            for ind in indices:
                if ind < lmi+1:
                    continue
                if sc == t[ind]:
                    lmi = ind
                    cnt += 1
                    break
        return len(s) == cnt    

    def t_map(self, t):
        t_char_ind_map = {}
        for ti, tc in enumerate(t):
            if tc not in t_char_ind_map:
                t_char_ind_map[tc] = set()
            t_char_ind_map[tc].add(ti)
        return t_char_ind_map