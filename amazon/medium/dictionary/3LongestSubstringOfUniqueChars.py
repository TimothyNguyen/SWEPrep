class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ans, l, r = 0, 0, 0
        largest_dict = dict()
        while r < len(s):
            if s[r] in largest_dict: 
                l = max(l, largest_dict[s[r]] + 1)
            ans = max(ans, r - l + 1)
            largest_dict[s[r]] = r
            r += 1
        return ans