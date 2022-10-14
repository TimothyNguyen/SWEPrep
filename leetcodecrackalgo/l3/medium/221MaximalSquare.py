'''
Given an m x n binary matrix filled with 0's and 1's, find the largest 
square containing only 1's and return its area.

Time/Space: O(mn)
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        max_ans = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(min(dp[r][c-1], dp[r-1][c]), dp[r-1][c-1]) + 1
                    max_ans = max(max_ans, dp[r][c])
        return max_ans * max_ans
        