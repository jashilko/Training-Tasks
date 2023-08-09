class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        for i in range(k):
            if s[i] in 'aeiou':
                max_count += 1
        i = k
        cnt = max_count
        while i <= len(s) - 1:
            if s[i] in 'aeiou':
                cnt += 1
            if s[i - k] in 'aeiou':
                cnt -= 1
            max_count = max(max_count, cnt)
            i += 1
        return max_count

if __name__ == "__main__":
    s = input()
    k =int( input())

    ss = Solution()
    print(ss.maxVowels(s, k))