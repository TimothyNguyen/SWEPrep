'''
Given an array of events where events[i] = 
[startDayi, endDayi]. Every event i starts at 
startDayi and ends at endDayi.

You can attend an event i at any day d where 
startTimei <= d <= endTimei. Notice that you can 
only attend one event at any time d.

Return the maximum number of events you can attend.

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
'''
import heapq
class Solution:
    def maxEvents(self, events) -> int:
        events.sort()
        final_date = 0
        for i in range(len(events)):
            final_date = max(final_date, events[i][1])
        heap = []  
        attended = 0
        ptr = 0
        heapq.heapify(heap)
        for curr_day in range(1, final_date + 1):
            while ptr < len(events) and events[ptr][0] == curr_day:
                heapq.heappush(heap, events[ptr][1])
                ptr += 1
            while heap and heap[0] < curr_day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                attended += 1
            
        return attended
    
soln = Solution()
# events = [[1,2],[2,3],[3,4]]
events = [[1, 3], [1, 4], [1, 5], [2,3],[3,4]]
print(soln.maxEvents(events))

# [[1, 3], [1, 4], [1, 5], [2,3],[3,4]]
'''
class Solution:
    def maxEvents(self, A: List[List[int]]) -> int:
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res
'''