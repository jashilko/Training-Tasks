class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n_word1 = ''.join((sorted(word1, key=str.lower)))
        n_word2 = ''.join((sorted(word2, key=str.lower)))
        if n_word1 == n_word2:
            return True
        elif len(word1) != len(word2):
            return False
        else:
            first = {}
            sec = {}
            for i in range(len(word1)):
               first[word1[i]] = first.get(word1[i], 0) + 1
               sec[word2[i]] = sec.get(word2[i], 0) + 1
            if set(first.keys()) == set(sec.keys()) and list(sorted(first.values())) == list(sorted(sec.values())):
                return True
            else:
                return False


if __name__ == "__main__":
    word1 = input()
    word2 = input()


    ss = Solution()
    print(ss.closeStrings(word1, word2))