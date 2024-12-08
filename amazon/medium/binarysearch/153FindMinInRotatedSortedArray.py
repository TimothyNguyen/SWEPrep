class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m + 1 < len(nums) - 1 and nums[m] > nums[m+1]:
                return nums[m + 1]
            if m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            elif nums[l] <= nums[m]:
                if nums[l] <= nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return min(nums[l], nums[r])