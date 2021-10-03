'''
Given an array of positive integers nums and a positive integer 
target, return the minimal length of a contiguous subarray 
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater 
than or equal to target. If there is no such subarray, return 0 instead.
'''
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
        
                
                
            