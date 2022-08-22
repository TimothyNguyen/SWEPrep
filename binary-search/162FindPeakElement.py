'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its 
index. If the array contains multiple peaks, return the index to 
any of the peaks.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should 
return the index number 2.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l