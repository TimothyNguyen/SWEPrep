'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
'''

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)