import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rotten_oranges = set()
        total_oranges = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.add((i, j))
                if grid[i][j] != 0:
                    total_oranges.add((i, j))
        
        ans = 0
        if len(total_oranges) == len(rotten_oranges):
            return ans 
        queue = collections.deque(rotten_oranges)
        while queue and len(total_oranges) != len(rotten_oranges):
            l = len(queue)
            for i in range(l):
                rotten_orange = queue.popleft()
                for (x, y) in dir_list:
                    new_x = x + rotten_orange[0]
                    new_y = y + rotten_orange[1]
                    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] != 1: 
                        continue
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
                    rotten_oranges.add((new_x, new_y))
            ans += 1
        return ans if len(total_oranges) == len(rotten_oranges) else -1
        

        
                    