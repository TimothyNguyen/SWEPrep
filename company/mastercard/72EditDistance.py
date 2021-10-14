class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if n * m == 0:
            return n + m
        
        # store dp
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i-1][j] + 1
                top = dp[i][j - 1] + 1
                left_top = dp[i-1][j-1]
                if word1[i - 1] != word2[j - 1]:
                    left_top += 1
                dp[i][j] = min(left, top, left_top)
        return dp[m][n]