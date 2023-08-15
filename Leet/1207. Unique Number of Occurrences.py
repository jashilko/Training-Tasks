from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uni_dict = {}
        for i in arr:
            uni_dict[i] = uni_dict.get(i, 0) + 1
        uni_set = set(uni_dict.values())
        return len(uni_set) == len(uni_dict)

if __name__ == "__main__":
    arr = list(map(int, input().split(',')))

    s = Solution()
    print(s.uniqueOccurrences(arr))