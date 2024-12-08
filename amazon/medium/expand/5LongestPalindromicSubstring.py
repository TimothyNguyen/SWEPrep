class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_palin(l, r) -> None:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        longest_str = ''
        for i in range(0, len(s)):
            s1 = longest_palin(i, i)
            s2 = longest_palin(i, i+1)
            if len(s1) >= len(longest_str) and len(s1) >= len(s2):
                longest_str = s1
            elif len(s2) >= len(longest_str) and len(s2) >= len(s1):
                longest_str = s2
        return longest_str