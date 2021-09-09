class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(ans)] != ans:
                ans = ans[:len(ans)-1]
                if len(ans) == 0: return ""
        return ans

# Test cases
# strs = ["flower", "flow", "flight"] -> "fl"