'''
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Case 1: Non-overlapping
        Case 2: Ovrlappingand the end point of the later interval fall before the end point of prev
        Case 3: Overlapping, but not like 2
        
        Great solutions but odd wording. If you have trouble understanding the 
        greedy solution (sort by start points) here is my version: if two intervals 
        are overlapping, we want to remove the interval that has the longer end point -- 
        the longer interval will always overlap with more or the same number of future 
        intervals compared to the shorter one

        Input: intervals = [[1,2],[1,3],[2,3],[3,4]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals 
        are non-overlapping.
        '''
        if len(intervals) == 0: 
            return 0
        intervals.sort(key=lambda x: x[0])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count