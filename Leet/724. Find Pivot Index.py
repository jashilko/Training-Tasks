from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        end_list = []
        sum = 0
        lenght = len(nums)
        for i in range(lenght):
            end_list.insert(0, sum)
            sum += nums[lenght - 1 - i]

        sum = 0
        begin_list = []
        for i in range(lenght):
            begin_list.append(sum)
            if sum == end_list[i]:
                return i
            sum += nums[i]
        return -1

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))

    s = Solution()
    print(s.pivotIndex(nums))