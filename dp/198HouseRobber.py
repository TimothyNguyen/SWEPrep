class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        memo = dict()
        
        def robFrom(i):
            if i >= len(nums): return 0
            if i in memo: return memo[i] # Return cached value
            
            # Recursive relation evaluation
            ans = max(robFrom(i+1), robFrom(i+2) + nums[i])
            memo[i] = ans
            return ans
        
        return robFrom(0)       
        '''
        currMax, prevMax = 0, 0
        for i in range(len(nums)):
            temp = currMax
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
        return currMax