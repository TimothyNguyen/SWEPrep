'''
Given an integer array nums, return the length of the longest 
strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array 
by deleting some or no elements without changing the order 
of the remaining elements. For example, [3,6,2,7] is a 
subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        max_ans = 1
        for i in range(1, len(dp)):
            max_val = 0
            for j in range(i):
                if nums[j] > nums[i]:
                    max_val = max(max_val, dp[j])
            dp[i] = max_val + 1
            max_ans = max(max_ans, dp[i])
        return max_ans

