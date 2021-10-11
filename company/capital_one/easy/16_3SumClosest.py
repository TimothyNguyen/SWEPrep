'''
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort() # O(n log n)
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if abs(total - target) < abs(ans-target):
                    ans = total
                if total <= target:
                    lo += 1
                else:
                    hi -= 1
            if total == target:
                break
        return ans
'''
[-4, -1, 1, 2]
  i   lo    hi
'''