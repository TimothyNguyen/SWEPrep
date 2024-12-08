class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        m, n = len(matrix), len(matrix[0])
        max_ans = 0
        dir_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            memo[(x, y)] = 0
            for (i, j) in dir_list:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                    memo[(x, y)] = max(memo[(x, y)], dfs(new_x, new_y))
            memo[(x, y)] += 1
            return memo[(x, y)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                max_ans = max(max_ans, dfs(r, c))
        return max_ans
