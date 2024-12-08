class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps_arr = [float('inf') for _ in nums]
        min_jumps_arr[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                min_jumps_arr[i] = 1
            elif nums[i] > 0:
                v = min(min_jumps_arr[i+1:i+nums[i]+1])
                if v != float('inf'):
                    min_jumps_arr[i] = int(v) + 1
        return min_jumps_arr[0]