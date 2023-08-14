from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = [[], []]
        for i in set1:
            if i not in set2:
                res[0].append(i)
        for i in set2:
            if i not in set1:
                res[1].append(i)
        return res

if __name__ == "__main__":
    nums1 = list(map(int, input().split(',')))
    nums2 = list(map(int, input().split(',')))

    s = Solution()
    print(s.findDifference(nums1, nums2))