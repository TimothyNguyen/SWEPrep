class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1: return res
        def dfs(path, start, target):
            if len(path) > 0:
                res.append(path + [target])
            for i in range(start, int(math.sqrt(target))+1): # i <= target//i, i.e., i <= sqrt(target)
                if target % i == 0:
                    dfs(path + [i], i, target // i)
        dfs([], 2, n)
        return res