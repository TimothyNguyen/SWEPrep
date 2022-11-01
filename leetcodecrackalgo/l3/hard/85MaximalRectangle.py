'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = 
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[0 for i in range(n)] for j in range(m)]
        maxarea = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    # compute the maximum width and update dp with it
                    width = dp[r][c] = dp[r][c-1] + 1 if c else 1
                    # compute the maximum area rectangle with a lower right corner at [i, j]
                    for k in range(r, -1, -1):
                        width = min(width, dp[k][c])
                        maxarea = max(maxarea, width*(r-k+1))
        return maxarea
class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea


    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea