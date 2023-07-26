class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_str = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if word1[i]:
                res_str += word1[i]
            if word2[i]:
                res_str += word2[i]
        res_str += word1[min_len:]
        res_str += word2[min_len:]
        return res_str

if __name__ == "__main__":
    word1 = input()
    word2 = input()

    s = Solution()
    print(s.mergeAlternately(word1, word2))