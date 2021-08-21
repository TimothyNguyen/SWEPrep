class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, l, r = 0, 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                maxarea = max(maxarea, height[l] * (r-l))
                l += 1
            else:
                maxarea = max(maxarea, height[r] * (r-l))
                r -= 1
        return maxarea