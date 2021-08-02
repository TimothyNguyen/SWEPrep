class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(res, tempList, start, remaining):
            if len(tempList) > k: return
            elif len(tempList) == k and remaining == 0: 
                res.append(list(tempList))
                return
            else:
                for i in range(start, 10):
                    tempList.append(i)
                    backtrack(res, tempList, i+1, remaining - i)
                    tempList.pop()
                    
        res = []
        backtrack(res, [], 1, n)
        return res