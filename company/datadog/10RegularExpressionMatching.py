'''
Given an input string s and a pattern p, implement regular expression 
matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

  a a
p 0 0
  a a
a 1 1
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[0 for _ in range(lenP)] for _ in range(lenS)]
        dp[0][0] = 1
        print(dp)
        for c in range(1, len(p)):
            if p[c] == '*':
                dp[0][c] = dp[0][c-2]

        for r in range(1, len(s)):
            for c in range(1, len(p)):
                if p[c] in {s[r], '.'}:
                    dp[r][c] = dp[r-1][c-1]
                elif p[c] == '*':
                    dp[r][c] = dp[r][c-2] or int(dp[r-1][c] and p[c-1] in {s[r], '.'})
        return bool(dp[-1][-1])