'''
There is an m x n rectangular island that borders both the Pacific 
Ocean and Atlantic Ocean. The Pacific Ocean touches the island's 
left and top edges, and the Atlantic Ocean touches the island's 
right and bottom edges.

The island is partitioned into a grid of square cells. You are 
given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water 
can flow to neighboring cells directly north, south, 
east, and west if the neighboring cell's height is less 
than or equal to the current cell's height. Water can 
flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where 
result[i] = [ri, ci] denotes that rain water can flow 
from cell (ri, ci) to both the Pacific and Atlantic oceans.

Time complexity: O(M⋅N), where M is the number of rows and N 
is the number of columns.
Similar to approach 1. The dfs function runs exactly once for each 
cell accessible from an ocean.

Space complexity: O(M⋅N), where M is the number of rows and N 
is the number of columns.

Similar to approach 1. Space that was used by our queues is now 
occupied by dfs calls on the recursion stack.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dir_cols = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        if not heights or not heights[0]:
            return []

        pacific_reachable, atlantic_reachable = set(), set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for (x, y) in dir_cols:
                new_row, new_col = r + x, c + y
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if (new_row, new_col) in reachable:
                    continue
                if heights[r][c] > heights[new_row][new_col]:
                    continue
                dfs(new_row, new_col, reachable)
        
        for r in range(m):
            dfs(r, 0, pacific_reachable)
            dfs(r, n-1, atlantic_reachable)
        for c in range(n):
            dfs(0, c, pacific_reachable)
            dfs(m-1, c, atlantic_reachable)
        return list(set.intersection(pacific_reachable, atlantic_reachable))