class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_inner(l: int, r: int) -> int:
            max_ans = nums[l]
            prev_max = 0
            for i in range(l + 1, r):
                temp_val = max_ans
                max_ans = max(max_ans, prev_max + nums[i])
                prev_max = temp_val
            return max_ans

        if len(nums) <= 2:
            return max(nums)

        ans1 = rob_inner(0, len(nums) - 1)
        ans2 = rob_inner(1, len(nums))
        return max(ans1, ans2)