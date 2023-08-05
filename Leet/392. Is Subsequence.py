class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j_s = 0
        if len(s)> 0:
            one_s = s[j_s]
        else:
            return True
        for one_t in t:
            if one_s == one_t:
                if j_s < len(s) - 1:
                    j_s += 1
                    one_s = s[j_s]
                else:
                    return True
        return False


if __name__ == "__main__":
    ss = input()
    tt = input()
    s = Solution()
    print(s.isSubsequence(ss, tt))

