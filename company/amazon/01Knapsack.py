'''
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
    0 1 2 3 4 5
1   0  
2   0  
3   0
5   0

Items can only be selected once
'''


def knapsack(weights, profits, capacity):
    ans = 0
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return ans
    dp = [[0] * (capacity + 1)] * len(profits)
    # Dp recursion 
    # dp[i][c] = max(dp[i-1][j], profits[i] + dp[i-1][c-weights[i]])
    for i in range(len(weights)):
        dp[i][0] = 0
    
    for c in range(c + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
        
    for i in range(1, len(profits)):
        for c in len(1, capacity + 1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            p2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(p1, p2)
    
    # maximum profit will be at the bottom-right corner.
    return dp[len(profits) - 1][capacity]