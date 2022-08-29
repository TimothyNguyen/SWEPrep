'''
Given an integer array nums that may contain duplicates, return all 
possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the 
solution in any order.

Basic idea:
    Sort nums first.
    Use a set data structure to add subsets (in the form of tuples) to ensure uniqueness.
    Use recursive DFS to traverse possible combinations

Big O:

    Time Complexity: O(N * 2^N)
    Space Complexity: O(N * 2^N)

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            """
            Utility function to DFS through nums list in tree-like fashion
            """
            res.add(tuple(path))
            for i in range(index, len(nums)): 
                dfs(i+1, path+[nums[i]])
        nums.sort()
        res = set()
        dfs(0, [])
        return list(res)