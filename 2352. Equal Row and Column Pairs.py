from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = {}
        col_dict = {}
        vert = []
        for i in range(len(grid)):
            #
            vert_row = []
            for j in range(len(grid)):
                vert_row.append(grid[j][i])
            vert.append(list(vert_row))
            vert_row.clear()
        for k in range(len(grid)):
            s = '&'.join(str(el) for el in grid[k])
            row_dict[s] = row_dict.get(s, 0) + 1
            s = '&'.join(str(el) for el in vert[k])
            col_dict[s] = col_dict.get(s, 0) + 1
        count = 0
        for key, value in row_dict.items():
            if key in col_dict:
                count += col_dict[key] * row_dict[key]
        #print(row_dict)
        #print(col_dict)
        return count
if __name__ == "__main__":
    grid = []
    for i in range(2):
        arr = list(map(int, input().split(',')))
        grid.append(arr)

    s = Solution()
    print(s.equalPairs(grid))