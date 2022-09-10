'''
Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
are being trapped.

Time: O(N)
Space: O(1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        l_max, r_max = 0, 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                water + max(0, l_max - height[l])
                l += 1
            else:
                r_max = max(r_max, height[r])
                water += max(0, r_max - height[r])
                r -= 1
        return water