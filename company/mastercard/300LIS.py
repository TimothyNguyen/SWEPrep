def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        max_ans = 1
        for i in range(1, len(dp)):
            max_val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            dp[i] = max_val + 1
            max_ans = max(max_ans, dp[i])
        return max_ans

# [10,9,2,5,3,7,101,18]