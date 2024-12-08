class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1]

class Solution:
    def change(self, n: int, coins: List[int]) -> int:
        # Memoization table to store number of ways for each (amount, coin_index)
        dp = {}

        # Helper function for recursion with memoization
        def helper(remaining, i):
            # If remaining amount is exactly 0, there is 1 way to make it (by using no coins)
            if remaining == 0:
                return 1
            # If remaining amount is negative, no valid way to make the amount
            if remaining < 0:
                return 0
            # If we've used all coins and haven't made the amount, return 0
            if i < 0:
                return 0
            # If result is already computed for this (remaining, i), return the stored result
            if (remaining, i) in dp:
                return dp[(remaining, i)]
            
            # Count ways by including current coin (coins[i]) and by excluding it
            include_coin = helper(remaining - coins[i], i)   # Use the coin again
            exclude_coin = helper(remaining, i - 1)          # Skip the coin
            
            # Store the result in dp table
            dp[(remaining, i)] = include_coin + exclude_coin
            return dp[(remaining, i)]

        # Compute the result for the original amount n and all coins
        return helper(n, len(coins) - 1)

'''
count_ways(amount - coins[i]) + count_ways(amount without coins)


[0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1]
[1, 1, 2, 2, 3, 3]
[0, 1, 2, 2, 3, 4]

[0, 0, 0, 0]
[0, 0, 1, 0]
[]
'''
'''
0 1 1 1 1 1
0 1 2 2 1 1
0 1 2 2 3 4
'''