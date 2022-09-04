'''
Given an array of integers heights representing the 
histogram's bar height where the width of each bar is 1, return the 
area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has 
an area = 10 units.
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # make right boundary
        heights.append(0)
        # store left boundary index
        stack = [-1] # tricky: -1 also denotes the left index of 0
        # keep track of max area
        area = 0
        # iterate through heights
        for idx, h in enumerate(heights):
            # we now find right boundary for stacks[-1]
            while h < heights[stack[-1]]:
                curr_idx = stack.pop()
                curr_h = heights[curr_idx]
                # right boundary (idx) is lower than 'curr_idx'
                right_boundary = idx
                # tricky part, note that every index stored in 'stack' 
                # is in ascending order, but not necessary continguous
                # also note that the reason we initially put '-1' in 
                # 'stack' is that -1 is instinctively left to 0, so 
                # it's naturally the left boundary for index 0
                left_boundary = stack[-1]
                curr_w = right_boundary - left_boundary - 1
                area = max(area, curr_h * curr_w)
            # we put every index to stack once
            # note that eventually every index except '-1' in stack will be popped out
            stack.append(idx)
        return area