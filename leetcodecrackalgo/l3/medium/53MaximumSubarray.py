'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        currentSubarray, maxSubarray = nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            currentSubarray = max(num, currentSubarray + num)
            maxSubarray = max(maxSubarray, currentSubarray)
        return maxSubarray