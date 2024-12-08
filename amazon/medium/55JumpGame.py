class Solution:
    def jumpGame(self, nums: List[int]) -> bool:
        furthest_jump = 0
        for i in range(0, len(nums)):
            if furthest_jump < i:
                return False
            furthest_jump = max(furthest_jump, i + nums[i])
        return furthest_jump >= len(nums) - 1