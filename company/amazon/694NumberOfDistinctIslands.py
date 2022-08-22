from enum import unique


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.add((row - row_o, col - col_o))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        seen = set()
        unique_islands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                current_island = set()
                row_o = r
                col_o = c
                dfs(r, c)
                if current_island:
                    unique_islands.add(frozenset(current_island))
        return len(unique_islands)