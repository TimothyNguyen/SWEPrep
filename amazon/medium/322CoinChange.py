class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for j in range(len(coins)):
            for i in range(coins[j], amount + 1):
                dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        def helper(amount):
            # if already computed, return result
            if dp[amount] != -1:
                return dp[amount]
            
            # Initialize min coins for this as inf
            min_coins_needed = float('inf')
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    result = helper(amount - coins[i])
                    if result != float('inf'):
                        min_coins_needed = min(min_coins_needed, result + 1)
            dp[amount] = min_coins_needed
            return dp[amount]
        
        result = helper(amount)
        return dp[-1] if result != float('inf') else -1
