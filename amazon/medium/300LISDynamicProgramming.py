class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxans = 1
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[l] < nums[r]:
                    dp[r] = max(dp[r], dp[l] + 1)
                    maxans = max(dp[r], maxans)
        return maxans