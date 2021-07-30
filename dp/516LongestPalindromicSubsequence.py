class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for c in s] for c in s]
        for i in range(len(s)):
            dp[i][i] = 1
        for startIndex in range(len(s) - 1, -1, -1):
            for endIndex in range(startIndex + 1, len(s)):
                if s[startIndex] == s[endIndex]:
                    dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex -1]
                else:
                    dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex],
                                                  dp[startIndex][endIndex - 1])
        return dp[0][len(s) - 1]
    