'''
Given an array of distinct integers candidates and a 
target integer target, return a list of all unique 
combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Let NN be the number of candidates, TT be the target value, and MM be the minimal value among the candidates.

Time Complexity: \mathcal{O}(N^(T/M + 1))
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(res, candidates, tempList, start, remaining):
            if remaining < 0: return
            elif remaining == 0: 
                res.append(list(tempList))
                return
            else:
                for i in range(start, len(candidates)):
                    tempList.append(candidates[i])
                    backtrack(res, candidates, tempList, i, remaining - candidates[i])
                    tempList.pop()
                    
        res = []
        sorted(candidates)
        backtrack(res, candidates, [], 0, target)
        return res