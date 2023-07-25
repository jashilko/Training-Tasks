from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        :type arr: List[int]
        :rtype: int
        """
        last = len(arr) - 1
        first = 0
        while 1==1:
            curr = int((last + first) // 2)
            # print(curr, arr[curr])
            if arr[curr] > arr[curr+1] and arr[curr] > arr[curr-1]:
                return curr
            if arr[curr] < arr[curr+1]:
                first = curr
            if arr[curr] < arr[curr-1]:
                last = curr


if __name__ == "__main__":
    arr = list(map(int, input().split(',')))
    s = Solution()
    print(s.peakIndexInMountainArray(arr))