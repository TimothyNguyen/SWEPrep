'''
Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit 
such that their cumulative weight is not more than a given number ‘C’. 

We can assume an infinite supply of item quantities; therefore, each item 
can be selected multiple times.

# O(N*C)
'''

def solve_knapsack(profits, weights, capacity):
    # TODO: Write your code here
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]
    for i in range(len(profits)):
        for w in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= w:
                profit1 = dp[i][w - weights[i]] + profits[i]
            if i > 0:
                profit2 = dp[i-1][w]
            dp[i][w] = max(profit1, profit2)
    return dp[len(profits) - 1][capacity]

def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
'''
      0 1  2  3  4  5  6   7   8
15 1 [0 15 30 45 60 75 90  105 120],
50 3 [0 15 30 50 65 80 100 115 130],
60 4 [0 ],
90 5 [0 ]
'''