'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        if not s or len(s) == 0:
            return ""
        l, r = 0, 0
        for i in range(len(s)):
            l1 = expandAroundCenter(s, i, i)
            l2 = expandAroundCenter(s, i, i+1)
            m = max(l1, l2)
            if m > r - l:
                l = i - (m - 1) // 2
                r = i + m // 2
        return s[l:r+1]
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1: return s
        dp = [[None for c in s] for c in s]
        longest = None
        for i in range(len(s)):
            dp[i][i] = True
        longest = [0, 1]

        for k in range(1,len(s)):
            for i in range(len(s)-k):
                j = i + k
                if k == 1:
                    is_p = s[i] == s[j]
                else:
                    is_p = s[i] == s[j] and dp[i+1][j-1]
                if is_p:
                    longest = dp[i, j + 1]
                dp[i][j] = is_p
        return s[longest[0]:longest[1]]
    