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