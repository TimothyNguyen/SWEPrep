'''
We have n jobs, where every job is scheduled to be done 
from startTime[i] to endTime[i], obtaining a profit of 
profit[i].

You're given the startTime, endTime and profit arrays, 
return the maximum profit you can take such that there 
are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be 
able to start another job that starts at time X.

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        events = []
        for i in range(n):
            # 1 for start event, 0 for end
            events.append((startTime[i], 1, i))
            events.append((endTime[i], 0, i))
        events.sort()

        maxProfit = [0] * n
        prev_max = 0

        for time, eventType, index in events:
            # If it's a start event, calculate max profit
            if eventType == 1:
                maxProfit[index] = prev_max + profit[index]
            else:
                prev_max = max(maxProfit[index], prev_max)
        return prev_max

# O(len(s_time) + len(end_time))