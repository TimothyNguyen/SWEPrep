class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0
    
        dp = [0] * len(height)
        highest_left = height[0]
        for i in range(1, len(height) - 1):
            dp[i] = highest_left
            highest_left = max(highest_left, height[i])
        
        highest_right = height[-1]
        for i in range(len(height) - 1, 0, -1):
            dp[i] = min(dp[i], highest_right)
            highest_right = max(highest_right, height[i])
            
        ans = 0
        for i in range(1, len(height) -1):
            ans += max(0, dp[i] - height[i]) 
        
        return ans