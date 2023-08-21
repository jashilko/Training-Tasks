class Solution:
    def decodeString(self, s: str) -> str:
        res_list = []
        temp_list = []
        counter = 0
        lenght = len(s) - 1
        i = lenght
        digit = []
        go = False
        while i >= 0 or go:
            if i >= 0 and s[i].isdigit():
                digit.append(s[i])
            else:
                if go:
                    digit.reverse()
                    temp_list = temp_list * int(''.join(digit))
                    if counter == 0:
                        res_list = res_list + temp_list
                        temp_list.clear()
                    go = False
                    digit.clear()
            if i >= 0:
                if s[i] == ']':
                    counter += 1
                elif s[i] == '[':
                    counter = counter - 1
                    go = True
                elif not s[i].isdigit():
                    if counter > 0:
                        temp_list.append(s[i])
                    else:
                        res_list.append(s[i])
            i = i -1

        res_list.reverse()
        return ''.join(res_list)



if __name__ == "__main__":

    s = input()
    ss = Solution()
    print(ss.decodeString(s))