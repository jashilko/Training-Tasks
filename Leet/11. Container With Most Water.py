from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        m_v = min(height[last], height[first]) * (last - first)
        while first < last:
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
            m_v = max(min(height[last], height[first]) * (last - first), m_v)
        return m_v


if __name__ == "__main__":
    height = list(map(int, input().split(',')))

    s = Solution()
    print(s.maxArea(height))