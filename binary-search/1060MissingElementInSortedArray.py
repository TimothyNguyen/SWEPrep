'''
Given an integer array nums which is sorted in ascending order and all of its 
are unique and given also an integer k, return the kth missing number starting
from the leftmost number of the array.

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def missing_nums(idx, nums):
            return nums[idx] - nums[0] - idx
        
        n = len(nums)
        
        if k > missing_nums(n-1, nums):
            return nums[n - 1] + k - missing_nums(n-1, nums)
        
        l, r = 0, n - 1
        while l != r:
            pivot = (l + r) // 2
            if missing_nums(pivot, nums) < k:
                l = pivot + 1
            else:
                r = pivot
        return nums[l - 1] + k - missing_nums(l-1, nums)
        
        '''
        # if kth missing number is larger than the last element in array
        if k > missing_nums(n-1, nums):
            return nums[n - 1] + k - missing_nums(n-1, nums)
        
        idx = 1
        while missing_nums(idx, nums) < k:
            idx += 1
        
        return nums[idx - 1] + k - missing_nums(idx-1, nums)
        '''