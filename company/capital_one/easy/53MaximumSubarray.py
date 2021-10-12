class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = nums[0]
        curr_ans = nums[0]
        for i in range(1, len(nums)):
            curr_ans = max(nums[i], nums[i] + curr_ans)
            max_ans = max(max_ans, curr_ans)
        return max_ans