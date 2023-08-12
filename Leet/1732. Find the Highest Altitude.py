from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hei = []
        hei.append(0)
        for i in range(len(gain)):
            hei.append(hei[i] + gain[i])
        return max(hei)

if __name__ == "__main__":
    gain = list(map(int, input().split(',')))

    s = Solution()
    print(s.largestAltitude(gain))