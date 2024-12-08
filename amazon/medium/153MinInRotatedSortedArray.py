class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            elif nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[0] < nums[m]:
                l = m + 1
            else:
                r = m - 1
'''
[4, 5, 6, 7, 0, 1, 2]
'''