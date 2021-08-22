'''
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = dict()
        def intBreak(n):
            if n <= 2:
                return 1
            if n in memo:
                return memo[n]
            ans = 1 * (n - 1)
            for i in range(2, n):
                firstNum = i
                secondNum = n - i
                product = firstNum * max(secondNum, intBreak(secondNum))
                if product > ans:
                    ans = product
            memo[n] = ans
            return ans
        ans = intBreak(n)
        return ans
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2 , n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i-j]))
        return dp[n]