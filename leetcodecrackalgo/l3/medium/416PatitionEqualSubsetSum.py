'''
Given a non-empty array nums containing only positive integers, find 
if the array can be partitioned into two subsets such that the sum of 
elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # if total_sum is odd, it cannot be partitioned 
        # into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        
        # construct dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[n][subset_sum]