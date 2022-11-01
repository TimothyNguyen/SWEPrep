'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1]. 

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
'''
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1: return res
        def dfs(path=[], start = 2, target=n):
            if len(path) > 0:
                res.append(path + [target])
            for i in range(start, int(math.sqrt(target))+1): # i <= target//i, i.e., i <= sqrt(target)
                if target % i == 0:
                    dfs(path + [i], i, target//i)
        dfs()
        return res