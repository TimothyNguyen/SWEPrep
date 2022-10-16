'''
nums = [1, 5, 2, 4, 6]
1 5 2 4 6

0 5 -3 7 -1
0 0 5 1 5
0 0 0 4 2
0 0 0 0 6
0 0 0 0 0

dp[3,4] = max((4-0), (6-0)) = 6
dp[2,3] = max((2-0), (4-0)) = 4
dp[2,4] = max((2-6), (6-4)) = 2
dp[1,2] = max((5-0), (2-0)) = 5
dp[2,3] = max((5-4), (4-5)) = 1
dp[1,2] = max((5-2), (6-1)) = 5
dp[0,1] = max((1-0), (5-0)) = 5
dp[0,2] = max((1-5), (2-5)) = -3
dp[0,3] = max((1-1), (4+3)) = 7
dp[0,4] = max((1-5), (6-7)) = -1
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0]*(len(nums) + 1) for i in range(len(nums) + 1)]
        for start in range(len(nums), -1, -1):
            for end in range(start, len(nums)):
                dp[start][end] = max(nums[start] - dp[start + 1][end] , nums[end] - dp[start][end - 1])       
        return dp[0][len(nums) - 1] >= 0
    
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = [[0]*len(nums) for i in range(len(nums))]
        def winner(start, end, turn):
            if start == end:
                return turn * nums[start]
            if memo[start][end]:
                return memo[start][end]
            a = turn * nums[start] + winner(start + 1, end, -turn)
            b = turn * nums[end] + winner(start, end - 1, -turn)
            memo[start][end] = turn * max(turn * a, turn * b)
            return memo[start][end]
        return winner(0, len(nums) - 1, 1) >= 0

                