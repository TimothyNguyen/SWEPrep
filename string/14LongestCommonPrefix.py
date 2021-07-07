class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        for i in range(1, len(strs)):
            while strs[i][0:len(ans)] != ans:
                ans = ans[0:len(ans)-1]
                if len(ans) == 0: return ""
        return ans
