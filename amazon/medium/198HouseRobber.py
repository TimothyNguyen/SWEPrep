class Solution:
    def rob(self, nums: List[int]) -> int:
        max_ans = nums[0]
        prev_max = 0
        for i in range(1, len(nums)):
            temp_val = max_ans
            max_ans = max(max_ans, prev_max + nums[i])
            prev_max = temp_val
        return max_ans