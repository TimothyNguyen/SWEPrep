class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while l <= r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += max(0, left_max - height[l])
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += max(0, right_max - height[r])
                r -= 1
        return water