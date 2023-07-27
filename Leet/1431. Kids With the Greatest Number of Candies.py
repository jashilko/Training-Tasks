from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m_kan = max(candies)
        #print(m_kan)
        res_list = []
        for child in candies:
            if child + extraCandies >= m_kan:
                res_list.append(True)
            else:
                res_list.append(False)
        return res_list

if __name__ == "__main__":
    candies = list(map(int, input().split(',')))
    extraCandies =int( input())

    s = Solution()
    print(s.kidsWithCandies(candies, extraCandies))