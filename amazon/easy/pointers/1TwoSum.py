class Solution:
    def twoSum(self, nums, target):
        sum_dict = dict()
        for i in range(len(nums)):
            if target - nums[i] in sum_dict:
                return [sum_dict[target - nums[i]], i]
            sum_dict[nums[i]] = i 
        return [-1, -1]