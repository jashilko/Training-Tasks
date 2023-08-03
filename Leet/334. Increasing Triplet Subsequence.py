from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = float('inf')
        two = float('inf')
        for i in nums:
            if i < one:
                one = i
            elif i < two and i > one:
                two = i
            elif i > two:
                return True

        return False

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    s = Solution()
    print(s.increasingTriplet(nums))