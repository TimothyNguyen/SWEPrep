'''
Given an m x n integers matrix, return the length of the longest 
increasing path in matrix.

From each cell, you can either move in four directions: left, 
right, up, or down. You may not move diagonally or move 
outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_ans = 0
        dir_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            for (dir_x, dir_y) in dir_list:
                new_dir = (i + dir_x,  j + dir_y)
                if 0 <= new_dir[0] < m and 0 <= new_dir[1] < n and matrix[new_dir[0]][new_dir[1]] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(new_dir[0], new_dir[1]))
            dp[i][j] += 1
            return dp[i][j]
        
        for x in range(m):
            for y in range(n):
                max_ans = max(max_ans, dfs(x, y)) 
        return max_ans