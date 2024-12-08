import bisect

# 

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)
        ends = [job[1] for job in jobs]

        for i in range(1, len(jobs) + 1):
            curr_profit = jobs[i-1][2]
            curr_start = jobs[i-1][0]

            last_non_overlapping_idx = bisect.bisect_right(ends, curr_start)

            dp[i] = max(dp[i-1], curr_profit + dp[last_non_overlapping_idx])
        return dp[-1]
        

'''
1. Sort jobs by end time
2. Use binary search potentially for the last non-overlapping job
    ends = [job[1] for job in jobs] 
    idx = bisect.bisect_left(ends, curr_idx)
3. DP table: dp[i] = max(dp[i-1], jobs[i-1][2] + dp[last remaining non])
- dp[i-1]: Skip the current job
- jobs[i-1][2] + dp[idx]: take the current job and add the profit from the last non-overlapping job

Input:
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

jobs => [[1, 3, 50], [2, 4, 10], [3, 5, 40], [3, 6, 70]]
ends => [3, 4, 5, 6]
dp = [0, 0, 0, 0, 0]

i = 1:
curr_profit = 50
curr_start = 1
last_remaining_on_overlap_idx = 0 
dp[1] = max(0, 50 + 0) = 50
dp = [0, 50, 0, 0, 0]


'''