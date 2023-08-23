class Solution:
    def decodeString(self, s: str) -> str:

        def recurseFunction(temp_s, i):
            res_str = ""

            while i <= len(temp_s) - 1:
                if temp_s[i].isdigit():
                    mult_str = ''
                    while temp_s[i].isdigit():
                        mult_str += temp_s[i]
                        i+=1
                    mult = int(mult_str)
                    ans, i = recurseFunction(temp_s, i+1)
                    res_str += mult * ans
                elif temp_s[i] == ']':
                    i += 1
                    return (res_str, i)
                else:
                    res_str = res_str + temp_s[i]
                    i += 1
            return (res_str, i)

        res_str, i = recurseFunction(s, 0)
        return res_str





if __name__ == "__main__":

    s = input()
    ss = Solution()
    print(ss.decodeString(s))