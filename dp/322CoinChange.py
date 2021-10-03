'''
You are given an integer array coins representing coins of 
different denominations and an integer amount representing a
total amount of money.

Return the fewest number of coins that you need to make up 
that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom up
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

'''
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''
# [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (coin 1)
# [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6] (coin 2) 
# [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3] (coin 2) 
# dp[x] = min(dp[j], dp[x - coin] + 1)
# Time: O(S * P)