'''
Given an array of meeting time intervals intervals where 
intervals[i] = [starti, endi], return the minimum number 
of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]

# After sort
[[0,30],[5,10],[15,20]]

# [30] 
# [10, 30]
# [20, 30]
Output: 2
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0: return 0
        intervals.sort(key = lambda x: x[0])
        allocator = []
        heapq.heappush(allocator, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= allocator[0]:
                heapq.heappop(allocator)
            heapq.heappush(allocator, intervals[i][1])
        return len(allocator)
    '''
    class Solution {
public int minMeetingRooms(int[][] intervals) {
    if (intervals == null || intervals.length == 0) {
        return 0;
    }
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    PriorityQueue<Integer> allocator = new PriorityQueue<>();
    allocator.add(intervals[0][1]);
    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= allocator.peek()) {
            allocator.poll();
        }
        allocator.add(intervals[i][1]);
    }
    return allocator.size();
}
}
    '''