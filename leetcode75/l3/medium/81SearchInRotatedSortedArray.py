class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0: return False
        l = 0 
        r = len(nums) - 1
        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: return True
            elif nums[m] > nums[l]:
                if target >= nums[l] and target < nums[m]: r = m
                else: l = m + 1
            elif nums[m] < nums[l]: # so l..r is sorted
                if target < nums[l] and target > nums[m]: l = m + 1
                else: r = m 
            else:
                l += 1
        return False