class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_ans = 0
        dir_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            for (i, j) in dir_list:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(new_x, new_y))
            dp[x][y] += 1
            return dp[x][y]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                max_ans = max(max_ans, dfs(r, c))
        return max_ans
