'''
Given a list of intervals calendar and a number of available conference rooms. 
For each query, return true if the meeting can be added to the calendar successfully 
without causing a conflict, otherwise false. A conference room can only hold 
one meeting at a time.

Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[2, 3], [3, 4]]
Output: [true, true]

Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[4, 5], [5, 6]]
Output: [false, true]

1. Find all the time intervals at which all meeting rooms are occupied, this can easily
done using dp: rooms[i] means rooms required at ith time. initially all set to 0
iterate over all intervals given.
2. Find all intervals with max number of meetings rooms and keep them in a sorted and non 
overlapping order.
3. Given a query [s, e], binary search for where this interval would fit and check if it 
intersects with interval on left or right.
'''

import heapq
class Solution:
    def meetingRooms(self, calendar, rooms, queries):

        def get_rooms(calendar):
            maxTime = max(interval[1] for interval in calendar)
            start, end = [0] * maxTime, [0] * maxTime
            for i in range(len(start)):
                start[i] = calendar[i][0]
                end[i] = calendar[i][1]
            start.sort()
            end.sort()
            res, endIdx = 0, 0
            for i in range(len(start)):
                if start[i] < end[endIdx]:
                    res += 1
                else:
                    endIdx += 1
            return res
        
        res = [False] * len(queries)
        lst = []
        for elem in calendar:
            lst.append(elem)
        for i in range(len(res)):
            lst.append(queries[i])
            if get_rooms(lst) <= rooms:
                res[i] = True
            lst.remove(len(list) - 1)
        return res
        '''
        maxTime = max([interval[1] for interval in calendar])
        meetings = [0] * (maxTime+1)
        ##1. record the events, start -> add one room; end -> remove one room
        for start, end in calendar:
            meetings[start] += 1
            meetings[end] -= 1

        ##2. get the rooms required for each time
        ##   e.g. meetings[3] = 2 means at the start of time 3, we require 2 rooms 
        for i in range(1, len(meetings)):
            meetings[i] += meetings[i-1]

        ##3. set the times to 1 when all available rooms are booked
        ##   e.g. meetings[3] = 1 means all rooms are booked during [3, 4] 
        for i in range(len(meetings)):
            if meetings[i] == rooms:
                meetings[i] = 1
            else:
                meetings[i] = 0

        ##4. get the cumulative count of times when all rooms are booked
        ##   e.g. meetings[6] = 3 means during [0, 7] all rooms are booked for a total of 3 hours
        for i in range(1, len(meetings)):
            meetings[i] += meetings[i-1]

        res = []
        ##5. [start, end] = [0, end] - [0, start]
        ##   to check whether we can book during [start, end], we just need to check if
        ##   the total amount of time when all rooms are booked has increased or not.
        for start, end in queries:
            if meetings[end-1] - meetings[start-1] > 0:
                res.append(False)
            else:
                res.append(True)
        return res 
        '''

'''
Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[2, 3], [3, 4]], queries = [[4, 5], [5, 6]]
[0, 1, -1, 0, 1, -1, 0, 0, 1, 0, -1]
[0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0]
[0, 1, 0, 0, 1, 0, 0, 0, 1, 2, 0]

'''