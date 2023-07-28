from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s_arr = sum(flowerbed)
        l_arr = len(flowerbed)
        if n == 0:
            return True
        elif l_arr // 2 - s_arr + 1 < n:
            return False
        else:
            # начинаем перебор
            flowerbed.append(0)
            flowerbed.insert(0, 0)
            for i in range(len(flowerbed) - 2):
                if flowerbed[i:i+3] == [0, 0, 0]:
                    n -= 1
                    flowerbed[i+1] = 1
                    if n == 0:
                        return True
            return False


if __name__ == "__main__":
    flowerbed = list(map(int, input().split(',')))
    n =int( input())

    s = Solution()
    s.canPlaceFlowers(flowerbed, n)