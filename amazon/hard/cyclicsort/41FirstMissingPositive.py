class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            # check if positive, in range, and not in correct position
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
'''
[3, 4, -1, 1] -> [-1, 4, 3, 1] (0, 2)
[-1, 4, 3, 1] -> [-1, 1, 3, 4] (1, 3)
[-1, 1, 3, 4] -> [1, -1, 3, 4] (0, 1)
'''