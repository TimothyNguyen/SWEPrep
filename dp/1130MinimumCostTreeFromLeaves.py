'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0: return 0
        return self.minSumOfNonLeafNodes(arr, 0, len(arr) - 1, {})
    
    def minSumOfNonLeafNodes(self, arr, i, j, memo):
        #if memo[i][j] != 0: return memo[i][j]
        if (i, j) in memo: return memo[(i, j)]
        if i >= j: return 0
        res = float('inf')
        for x in range(i, j):
            l = self.minSumOfNonLeafNodes(arr, i, x, memo)
            r = self.minSumOfNonLeafNodes(arr, x + 1, j, memo)
            maxleft, maxright = 0, 0
            for idx in range(i, x+1): maxleft = max(maxleft, arr[idx])
            for idx in range(x+1, j+1): maxright = max(maxright, arr[idx])
            valueOfNonLeafNode = maxright * maxleft
            res = min(res, valueOfNonLeafNode + l + r)
        memo[(i, j)] = res
        return res 
'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]