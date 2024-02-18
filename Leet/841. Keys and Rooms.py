from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        for i in range(len(rooms)):
            visited[i] = False
        self.v_count = 0
        def dfs(graph: List, visited: dict, now: int):
            visited[now] = True
            self.v_count += 1
            for neig in graph[now]:
                if not visited[neig]:
                    dfs(graph, visited, neig)
        dfs(rooms, visited, 0)
        if self.v_count == len(rooms):
            return True
        else:
            return False


if __name__ == "__main__":

    #rooms = [[1], [2], [3], []]
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    s = Solution()
    print(s.canVisitAllRooms(rooms))