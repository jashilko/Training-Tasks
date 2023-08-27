from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        i = 0
        while i < len(senate):
            if senate[i] == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
            i += 1
        while r_queue and d_queue:
            r_first = r_queue.popleft()
            d_first = d_queue.popleft()
            if r_first < d_first:
                r_queue.append(i)
            else:
                d_queue.append(i)
            i += 1
        if r_queue:
            return "Radiant"
        else:
            return "Dire"



if __name__ == "__main__":
    senate = input()

    s = Solution()
    print(s.predictPartyVictory(senate))