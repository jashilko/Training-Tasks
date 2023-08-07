from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_list = sum(matrix, [])
        #бинарный поиск
        first = 0
        last = len(new_list) - 1
        while first <= last:
            cur = (last + first) // 2
            if new_list[cur] == target:
                return True
            elif new_list[cur] < target:
                first = cur + 1
            elif new_list[cur] > target:
                last = cur - 1
        return False


if __name__ == "__main__":
    matrix = []
    for _ in range(2):
        one = list(map(int, input().split(',')))
        matrix.append(one)
    target = int(input())
    s = Solution()
    print(s.searchMatrix(matrix, target))