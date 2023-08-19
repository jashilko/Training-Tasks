from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res_list = []
        for cur in asteroids:
            not_get = 0
            while not not_get:
                len_res = len(res_list)
                if len_res == 0:
                    res_list.append(cur)
                    not_get = 1
                else:
                    prev = res_list[len_res - 1]
                    if prev > 0 and cur < 0:
                        if abs(prev) > abs(cur):
                            not_get = 1
                        elif abs(prev) == abs(cur):
                            res_list.pop()
                            not_get = 1
                        else:
                            res_list.pop()

                    else:
                        res_list.append(cur)
                        not_get = 1
        return  res_list

if __name__ == "__main__":

    arr = list(map(int, input().split(',')))


    s = Solution()
    print(s.asteroidCollision(arr))