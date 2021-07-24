class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
                right -= 1
        return water

'''
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
'''