class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        arr[0] = 1
        for i in range(1, len(nums)):
            arr[i] = nums[i - 1] * arr[i - 1]
        R = 1
        for i in reversed(range(len(nums))):
            arr[i] = arr[i] * R
            R *= nums[i]
        return arr
            