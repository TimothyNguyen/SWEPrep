class Solution(object):
    def longestCommonSuffix(self, strs):
        ans = strs[0]
        idx = 0
        for i in range(1, len(strs)):
            if ans != strs[i][idx:len(ans)]:
                ans = ans[1:]
                idx += 1
                if len(ans) == 0: break
        return ans
