class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        left_min, right_max = prices[0], prices[-1]
        
        left_profits, right_profits = [0] * len(prices), [0] * (len(prices) + 1)
        
        # Construct the bidirectional dp array
        for l in range(1, len(prices)):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])
            
            r = len(prices) - l - 1
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])
        return max_profit