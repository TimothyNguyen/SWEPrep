class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        while l <= r:
            if height[l] >= height[r]:
                maxarea = max(maxarea, height[r] * (r-l))
                r -= 1
            else:
                maxarea = max(maxarea, height[l] * (r-l))
                l += 1
        return maxarea