'''
You are starving and you want to eat food as quickly as possible. You want to 
find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your 
current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If 
there is no path for you to reach food, return -1.
'''
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
    