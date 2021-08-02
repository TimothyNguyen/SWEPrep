# Given a collection of numbers, nums, that 
# might contain duplicates, return all possible 
# unique permutations in any order.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permuteSet = set()
        def backtrack(i):
            if i == len(nums) and ''.join(str(nums)) not in permuteSet:
                sol.append(list(nums))
                permuteSet.add(''.join(str(nums)))
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        sol = []
        backtrack(0)
        return sol