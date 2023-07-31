from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 0
        null_count = 0
        has_not_null = False
        for i in nums:
            if i != 0:
                if not has_not_null:
                    has_not_null = True
                    mult = 1
                mult *= i
            else:
                null_count += 1
        res_list = []
        for i in nums:
            if null_count == 0:
                res_list.append(int(mult / i))
            elif null_count == 1:
                if i == 0:
                    res_list.append(mult)
                else:
                    res_list.append(0)
            else:
                res_list.append(0)
        return res_list

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    s = Solution()
    print(s.productExceptSelf(nums))