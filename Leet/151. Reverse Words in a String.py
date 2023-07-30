class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        s_res = ""
        for one in s_list:
            if one:
                s_res = one + " " + s_res
        return s_res.rstrip()

if __name__ == "__main__":
    st = input()
    s = Solution()
    print(s.reverseWords(st))