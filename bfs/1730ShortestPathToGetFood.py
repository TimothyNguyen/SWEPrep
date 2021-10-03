class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        start = '*'
        food = '#'
        wall = 'X'
        
        queue = []
        m, n = len(grid), len(grid[0])
        
        # Find the starting point
        for r in range(m):
            for c in range(n):
                if grid[r][c] == start:
                    queue.append((r, c))
                    grid[r][c] = wall
                    break
        
        if len(queue) == 0: return -1
        
        # Run bfs
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
        steps = 0
        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                row, col = queue.pop(0)
                
                for dr, dc in dirs:
                    new_r = row + dr
                    new_c = col + dc
                    if new_r == m or new_c == n or new_r < 0 or new_c < 0 or grid[new_r][new_c] == wall:
                        continue
                    
                    if grid[new_r][new_c] == '#':
                        return steps + 1
                    
                    queue.append((new_r, new_c))
                    grid[new_r][new_c] = wall # visited
            
            steps += 1
        return - 1
    