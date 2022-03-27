def lengthOfLIS(self, nums: List[int]) -> int:
        '''
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
        '''
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
# [10,9,2,5,3,7,101,18]