class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_num = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far*curr)
            temp_min = min(curr, max_so_far * curr, min_so_far*curr)
            min_so_far = temp_min
            max_so_far = temp_max
            max_num = max(max_num, max_so_far, min_so_far)
        return max_num