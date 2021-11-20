class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                water += max(0, l_max - height[l])
                l += 1
            else:
                r_max = max(r_max, height[r])
                water += max(0, r_max - height[r])
                r -= 1
        return water