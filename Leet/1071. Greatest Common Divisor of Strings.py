class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        # Строка 1 всегда должна быть меньше
        if len2 < len1:
            str = str1
            str1 = str2
            str2 = str
            ll = len1
            len1 = len2
            len2 = ll
        for i in range(len1):
            if str1.count(str1[:len1-i]) == len1/(len1-i) and str2.count(str1[:len1-i]) == len2/(len1-i):
                return str1[:len1-i]
        return ""


if __name__ == "__main__":
    str1 = input()
    str2 = input()

    s = Solution()
    print(s.gcdOfStrings(str1, str2))