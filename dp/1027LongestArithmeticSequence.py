class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 2
        n = len(nums)
        dp = [{} for _ in range(n)] 
        for j in range(n):
            for i in range(j):
                d = nums[j] - nums[i]
                # print(dp)
                if d not in dp[i]:
                    dp[i][d] = 1
                dp[j][d] = dp[i][d] + 1
                res = max(res, dp[j][d])
        return res