from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt_k = 0

        end = 0

        cnt_1 = 0

        while cnt_k <= k and end < len(nums):
            if nums[end] == 0:
                if cnt_k == k:
                    break
                else:
                    cnt_k += 1
            cnt_1 += 1
            end += 1
        max_cnt_1 = cnt_1
        #list_of_one.append(cnt_1)
        begin = 1

        while end < len(nums):
            if nums[begin - 1] == 0:
                cnt_k -= 1
            else:
                cnt_1 -= 1
            while cnt_k <= k and end < len(nums):
                if nums[end] == 1:
                    cnt_1 += 1
                elif cnt_k < k:
                    cnt_k += 1
                else:
                    begin += 1
                    break
                end += 1
            max_cnt_1 = max(max_cnt_1, cnt_1)
        #print(list_of_one)
        return max_cnt_1

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    k =int( input())

    s = Solution()
    print(s.longestOnes(nums, k))
