class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for r in range(len(grid)):
            grid[r][0] = 1
        for c in range(len(grid[0])):
            grid[0][c] = 1
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[-1][-1]