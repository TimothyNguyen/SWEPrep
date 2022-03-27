'''
Given an input string (s) and a pattern (p), implement wildcard 
pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
'''
class Solution:
    def isMatch(self, s, p):
        s, p = ' ' + s, ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[0 for _ in range(lenP)] for _ in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
            if p[j] != '*':
                break
            dp[0][j] = 1
        
        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return bool(dp[-1][-1])