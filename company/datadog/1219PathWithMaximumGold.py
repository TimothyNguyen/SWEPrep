# O(M*N)^2
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        self.max_gold = 0
        def dfs(row, col, curgold):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] > 0:
                temp = grid[row][col]
                grid[row][col] = 0
                dfs(row - 1, col, curgold + temp)
                dfs(row + 1, col, curgold + temp)
                dfs(row, col - 1, curgold + temp)
                dfs(row, col + 1, curgold + temp)
                self.max_gold = max(self.max_gold, curgold + temp)
                grid[row][col] = temp
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.max_gold