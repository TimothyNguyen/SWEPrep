'''
There is an m x n rectangular island that borders both the Pacific Ocean 
and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n 
integer matrix heights where heights[r][c] represents the height above sea level 
of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring 
cells directly north, south, east, and west if the neighboring cell's height 
is less than or equal to the current cell's height. Water can flow from any 
cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific 
and Atlantic oceans.

Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Time complexity: O(M⋅N), where M is the number of rows and N 
is the number of columns.

Similar to approach 1. The dfs function runs exactly 
once for each cell accessible from an ocean.

Space complexity: O(M⋅N), where M is the number of rows and N 
is the number of columns.
'''

class Solution:
    def pacificAtlantic(self, matrix):
        m, n = len(matrix), len(matrix[0])

        dir_cols = [(1,0), (-1, 0), (0, 1), (0, -1)]
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
        pacific_reachable, atlantic_reachable = set(), set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for (x, y) in dir_cols:
                new_r, new_c = r + x, c + y
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n: continue
                if (new_r, new_c) in reachable: continue
                if matrix[r][c] > matrix[new_r][new_c]: continue
                dfs(new_r, new_c, reachable)
        
        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)
        for i in range(n):
            dfs(0, i, pacific_reachable)
            dfs(m - 1, i, atlantic_reachable)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            if (r, c) in reachable or r < 0 or c < 0 or r > len(heights) - 1 or \
                c > len(heights[0]) - 1:
                return
            reachable.add((r, c))
            temp_val = heights[r][c]
            heights[r][c] = 10**5 + 1
            if r == 0 or temp_val <= heights[r-1][c]:
                dfs(r-1, c, reachable)
            if c == 0 or temp_val <= heights[r][c-1]:
                dfs(r, c-1, reachable)
            if r == len(heights) - 1 or temp_val <= heights[r+1][c]:
                dfs(r+1, c, reachable)
            if c == len(heights[0]) - 1 or temp_val <= heights[r][c+1]:
                dfs(r, c+1, reachable)
            heights[r][c] = temp_val

        for r in range(len(heights)):
            dfs(r, 0, pacific_reachable)
            dfs(r, len(heights[0])-1, atlantic_reachable)
        for c in range(len(heights[0])):
            dfs(0, c, pacific_reachable)
            dfs(len(heights) - 1, c, atlantic_reachable)
        
        print(atlantic_reachable)
        print(pacific_reachable)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                    res.append([r,c])
        return res
        
        # return list(pacific_reachable.intersection(atlantic_reachable))