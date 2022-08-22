class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for x_start, x_end in points:
            if end < x_start:
                arrows += 1
                end = x_end
        return arrows
# [[1, 6], [2, 8], [7, 12], [10, 16]]