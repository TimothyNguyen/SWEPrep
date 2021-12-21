'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[0 for _ in range(lenP)] for _ in range(lenS)]
        dp[0][0] = 1
        for j in range(1, lenP):
            if p[j] != '*':
                break
            else:
                dp[0][j] = 1
        
        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return bool(dp[-1][-1])
        