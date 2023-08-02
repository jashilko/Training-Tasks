from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(len(nums)):
            if nums[j] == 0:
                el = nums.pop(j)
                nums.append(el)

            else:
                j += 1
        return nums

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    s = Solution()
    print(s.moveZeroes(nums))