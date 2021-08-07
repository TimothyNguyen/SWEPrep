class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        non_decrease_count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if non_decrease_count == 1: 
                    return False
                non_decrease_count += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
        