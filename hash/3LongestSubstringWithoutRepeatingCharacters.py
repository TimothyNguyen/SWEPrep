class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        map = dict()
        i, j = 0, 0
        while j < len(n):
            if s[j] in map:
                i = max(map[s[j]], i)
            ans = max(ans, j - i + 1)
            map[s[j]] = j + 1
            j += 1
        return ans
    
        