'''
Given a sorted array of distinct integers and a target value, return 
the index if the target is found. If not, return the index where it 
would be if it were inserted in order.
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target: r = m - 1
            elif nums[m] < target: l = m + 1
            else: return m
        return l