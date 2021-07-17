class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dir_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        # Find all the rotten oranges
        visited = set()
        total_oranges = set()
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    visited.add((r, c))
                if grid[r][c] != 0:
                     total_oranges.add((r, c))
                        
        queue = deque(visited)
        ans = 0
        if len(total_oranges) == len(visited):
            return ans
        while queue:
            l = len(queue)
            for i in range(l):
                rotten_orange = queue.popleft()
                for (x, y) in dir_list:
                    new_x = x + rotten_orange[0]
                    new_y = y + rotten_orange[1]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] != 1: continue
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
            ans += 1
            if len(total_oranges) == len(visited):
                return ans
        return ans if len(total_oranges) == len(visited) else -1
    
        
            
        