# Given an array nums of distinct integers, return all the 
# possible permutations. You can return the answer in 
# any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i):
            if i == len(nums):
                sol.append(list(nums))
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        sol = []
        backtrack(0)
        return sol