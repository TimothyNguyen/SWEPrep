'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Tmap = Counter(t)
        matchMap = Counter()

        if len(s) < len(t):
            return ""

        start, end = 0, 0
        minStr = []
        minLen = float('inf')

        while start <= end <= len(s):
            if not Tmap - matchMap:
                if minLen >= (end - start):
                    minStr = list(s[start:end])
                    minLen = len(minStr)
                matchMap.subtract(s[start])
                start += 1
            else:
                if end < len(s):
                    matchMap.update(s[end])
                end += 1

        return ''.join(minStr) 