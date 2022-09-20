class Solution:
    def findMax(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1 or nums[r] > nums[l]:
            return nums[r]
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m]
            if nums[m - 1] > nums[m]:
                return nums[m - 1]
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1
        return nums[r]