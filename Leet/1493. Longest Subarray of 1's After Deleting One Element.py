from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt_0 = 0
        cnt_1 = 0
        cnt_1_max = 0
        begin = 0
        end = 0
        was_0 = False
        while cnt_0 < 2 and end < len(nums):
            if nums[end] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_0 < 2:
                end += 1
            else:
                break
        cnt_1_max = cnt_1
        if cnt_0 > 0:
            was_0 = True
        while end < len(nums):
            if cnt_0 == 2:
                if nums[begin] == 0:
                    cnt_0 -= 1
                else:
                    cnt_1 -= 1
                begin += 1
            if cnt_0 < 2:
                if end < len(nums) -1 and nums[end + 1] == 1:
                    cnt_1 += 1
                else:
                    cnt_0 += 1
                end += 1
            if cnt_1 > cnt_1_max:
                cnt_1_max = cnt_1
                if cnt_0 > 0:
                    was_0 = True
                else:
                    was_0 = False
        if was_0:
            return cnt_1_max
        else:
            return cnt_1_max - 1

if __name__ == "__main__":
    arr = list(map(int, input().split(',')))
    s = Solution()
    print(s.longestSubarray(arr))