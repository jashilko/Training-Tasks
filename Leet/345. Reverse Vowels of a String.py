class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        first_vow = ''
        last_vowels = ''
        first = 0
        last = len(s_list) - 1
        while last > first:
            if first_vow and last_vowels:
                s_list[first] = last_vowels
                s_list[last] = first_vow
                last_vowels = ''
                first_vow = ''
                first += 1
                last -= 1
            else:
                if s_list[first] in vowels:
                    first_vow = s_list[first]
                else:
                    first += 1
                if s_list[last] in vowels:
                    last_vowels = s_list[last]
                else:
                    last -= 1
        new_str = ''.join(s_list)
        #print(new_str)
        return new_str


if __name__ == "__main__":

    st = input()

    s = Solution()
    s.reverseVowels(st)