class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            num_blocks = 0
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
                return num_blocks
            num_blocks += 1
            grid[x][y] = '0'
            return num_blocks + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
        num_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                num_islands += 1 if dfs(x, y) > 0 else 0
        return num_islands
