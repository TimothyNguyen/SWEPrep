class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        events = []
        for i in range(n):
            events.append((startTime[i], 1, i))
            events.append((endTime[i], 0, i))
            
        events.sort()
        maxProfit = [0] * n
        prev_max = 0
        
        for time, eventType, index in events:
            if eventType == 1:
                maxProfit[index] = prev_max + profit[index]
            else:
                prev_max = max(maxProfit[index], prev_max)
        return prev_max