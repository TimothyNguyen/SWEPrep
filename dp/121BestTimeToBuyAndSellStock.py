class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_curr_num = float('inf')
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, prices[i] - smallest_curr_num)
            smallest_curr_num = min(smallest_curr_num, prices[i])
        return ans