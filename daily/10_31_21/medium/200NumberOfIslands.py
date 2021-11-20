'''
Given an m x n 2D binary grid grid which represents a map 
of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all 
surrounded by water.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        return num_islands