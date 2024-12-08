class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        sol = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= sol[-1][1]:
                sol[-1][1] = max(intervals[i][1], sol[-1][1])
            else:
                sol.append(intervals[i])
        return sol