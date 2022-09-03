# Given a collection of numbers, nums, that 
# might contain duplicates, return all possible 
# unique permutations in any order.
'''
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
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results