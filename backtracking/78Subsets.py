'''
Given an integer array nums of unique elements, return all possible subsets 
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]



Time complexity: O(N×2N) to generate all subsets and then copy them into output list.
Space complexity: O(N) e are using O(N) space to maintain curr, and are modifying 
curr in-place with backtracking. Note that for space complexity analysis, we do 
not count space that is only used for the purpose of returning output, so the 
output array is ignored.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr):
            if k == len(curr):
                output.append(list(curr))
                return
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
        return output