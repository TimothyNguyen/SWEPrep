'''
Given two strings text1 and text2, return the length of their 
longest common subsequence. If there is no common subsequence, 
return 0.

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp_grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp_grid[i][j] = 1 + dp_grid[i-1][j-1]
                else:
                    dp_grid[i][j] = max(dp_grid[i-1][j], dp_grid[i][j-1])
        return dp_grid[m][n]
'''
  a b c d e
a 1 1 1 1 1
c 1 1 2 2 2 
e 1 1 2 2 3
'''