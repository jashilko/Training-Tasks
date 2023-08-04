from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        start_len = len(chars)

        simb = chars[0]
        count = 0
        total_count = 0
        j = 0
        len_s = len(chars)
        while j < len_s:
            if chars[0] == simb:
                count += 1
            else:
                total_count += 1
                chars.append(simb)
                if count > 1:
                    total_count += len(str(count))
                    for i in str(count):
                        chars.append(i)
                simb = chars[0]
                count = 1
            j += 1
            chars.pop(0)


        chars.append(simb)
        if count > 1:
            total_count += len(str(count))
            for i in str(count):
                chars.append(i)
        #print(chars)
        #return chars


if __name__ == "__main__":
    chars = list(input().split(','))
    s = Solution()
    print(s.compress(chars))