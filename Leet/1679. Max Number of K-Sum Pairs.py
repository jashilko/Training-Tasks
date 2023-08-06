from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        begin = 0
        end_p = len(nums) - 1
        nums.sort()
        sum_minus = 0
        while begin < end_p:
            if nums[begin] + nums[end_p] < k:
                begin += 1
            elif nums[begin] + nums[end_p] > k:
                end_p -= 1
            else:
                sum_minus += 1
                begin += 1
                end_p -= 1
        return sum_minus

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    k = int(input())
    s = Solution()
    print(s.maxOperations(nums, k))