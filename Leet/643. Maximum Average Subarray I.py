from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[0:k])
        av = summ / k
        i = k
        while i <= len(nums) - 1:
            summ = summ + nums[i] - nums[i-k]
            av = max(summ/k, av)
            i += 1
        return av

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    k =int( input())

    s = Solution()
    print(s.findMaxAverage(nums, k))