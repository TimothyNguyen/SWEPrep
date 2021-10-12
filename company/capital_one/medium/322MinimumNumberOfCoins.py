class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for w in range(coin, amount + 1):
                dp[w] = min(dp[w], dp[w - coin] + 1) 
        return dp[amount] if dp[amount] != float('inf') else -1
        

# [1, 2, 5], amount = 11
'''
[0 1 2 3 4 5 6 7 8 9 10 11]
[0 1 1 2 0 0 0 0 0 0  0  0]
'''