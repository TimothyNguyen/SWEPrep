class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]
            
    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right 
inclusive where left <= right.

Implement the NumArray class:
    - NumArray(int[] nums) Initializes the object with the integer array nums.
    - int sumRange(int left, int right) Returns the sum of the elements 
    of nums between indices left and right inclusive 
    (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''