class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        max_arr, min_arr = [0] * len(nums), [0] * len(nums)
        max_arr[0], min_arr[0] = nums[0], nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                min_arr[i] = min(nums[i], min_arr[i-1]*nums[i])
                max_arr[i] = max(nums[i], max_arr[i-1]*nums[i])
            else:
                min_arr[i] = min(nums[i], max_arr[i-1]*nums[i])
                max_arr[i] = max(nums[i], min_arr[i-1]*nums[i])
            result = max(result, max_arr[i])
        return result