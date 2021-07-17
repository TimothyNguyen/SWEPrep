class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        # First get a running sum
        min_ans = float("inf")
        # Do the 2 pointer method
        subarray_sum = 0
        for r in range(len(nums)):
            subarray_sum += nums[r]
            while subarray_sum >= target:
                min_ans = min(r - l + 1, min_ans)
                subarray_sum -= nums[l]
                l += 1 
        return min_ans if min_ans != float("inf") else 0
        
                
                
            