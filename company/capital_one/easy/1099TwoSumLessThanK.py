class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_ans = -1
        while l < r:
            if nums[l] + nums[r] < k:
                max_ans = max(max_ans, nums[l] + nums[r])
                l += 1
            else:
                r -= 1
        return max_ans