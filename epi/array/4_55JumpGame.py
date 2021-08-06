class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or (nums[0] == 0 and len(nums) != 1): return False
        furthest_dist, r = 0, len(nums) - 1
        i = 0
        while i <= furthest_dist and furthest_dist <= r:
            furthest_dist = max(furthest_dist, nums[i] + i)
            i += 1
        return furthest_dist >= r