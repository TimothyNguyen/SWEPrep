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