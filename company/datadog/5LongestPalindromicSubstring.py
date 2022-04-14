class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s
        
        def around_center(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
    
        i = 0
        l, r = 0, 0
        while i < len(s):
            len1 = around_center(i, i, s)
            len2 = around_center(i, i + 1, s)
            curr_len = max(len1, len2)
            if curr_len > r - l:
                # "cbbd"
                l = i - (curr_len - 1) // 2
                r = i + curr_len // 2
            i += 1
        return s[l:r+1]