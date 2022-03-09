'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def twoSumII(i: int):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0: l += 1
                elif sum > 0: r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)
        return res
'''
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(k, nums, target):
            res = []
            if not nums:
                return res
            
            average_value = target // k
            
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for part_arr in kSum(k - 1, nums[i + 1:], target - nums[i]):
                        res.append([nums[i]] + part_arr)
            return res
        
        
        def twoSum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1
            
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
                    
            
        nums.sort()
        return kSum(3, nums, target)
        
        
# [-2, -1, 0, 0, 1, 2]