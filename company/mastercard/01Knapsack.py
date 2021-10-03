# Given weights and values of n items, put these items in a 
# knapsack of capacity W to get the max total value in the 
# knapsack.

# value[] = { 60, 100, 120 };
# weight[] = { 10, 20, 30 };
# W = 50 -> 220
# dp[i][c] = max (dp[i-1][c], profits[i] + dp[i-1][c-weights[i]]) 
# Time/Space: 0(S*C)
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it's not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # Include the item, if it's not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            # exclude item
            profit2 = dp[i-1][c]
            # take max
            dp[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]

def knapsack(weights, values, capacity):
    dp = [0 for i in range(capacity + 1)]
    for i in range(1, len(weights)):
        for w in range(capacity, 0, -1):
            # WTF 
            if weights[i - 1] <= w:
                dp[w] = max(dp[w], dp[w-weights[i-1]] + values[i-1])
    return dp[len(weights)]

# [0, 1, 2, 3, 4, 5]
# [0, 0, 0, 0, 0, ]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()