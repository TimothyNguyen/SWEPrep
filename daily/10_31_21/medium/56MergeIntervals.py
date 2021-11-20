'''
Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s1 = []
        intervals.sort(key = lambda x: x[0])
        while intervals:
            new_interval = intervals.pop()
            if not s1 or s1[-1][1] < new_interval[0]:
                s1.append(new_interval)
            else:
                s1[-1][1] = max(s1[-1][1], new_interval[1])
        return s1