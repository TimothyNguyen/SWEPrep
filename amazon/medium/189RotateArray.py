class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        k = k % len(nums)
        start = count = 0
        while count < len(nums):
            curr_idx, prev = start, nums[start]
            while True:
                next_idx = (curr_idx + k) % len(nums)
                nums[next_idx], prev = prev, nums[next_idx]
                curr_idx = next_idx
                count += 1
                if start == curr_idx:
                    break
            start += 1
        return nums

'''
Example 1, k = 3
[1, 2, 3, 4, 5, 6, 7] prev = 1, curr_idx = 0, count = 0, start = 0
[1, 2, 3, 1, 5, 6, 7] prev = 4, curr_idx = 3, count = 1, start = 0
[1, 2, 3, 1, 5, 6, 4] prev = 7, curr_idx = 6, count = 2, start = 0
[1, 2, 7, 1, 5, 6, 4] prev = 3, curr_idx = 2, count = 3, start = 0
[1, 2, 7, 1, 5, 3, 4] prev = 6, curr_idx = 5, count = 4, start = 0
[1, 6, 7, 1, 5, 3, 4] prev = 2, curr_idx = 1, count = 5, start = 0
[1, 6, 7, 1, 2, 3, 4] prev = 5, curr_idx = 4, count = 6, start = 0
[5, 6, 7, 1, 2, 3, 4] prev = 1, curr_idx = 0, count = 7, start = 0

Example 2, k = 2
[-1,-100,3,99] prev = -1, curr_idx = 0, count = 0, start = 0
[-1, -100, -1, 99] prev = 3, curr_idx = 2, count = 1, start = 0
[3, -100, -1, 99] prev = -100, curr_idx = 1, count = 2, start = 1
[3, -100, -1, -100] prev = 99, curr_idx = 3, count = 3, start = 1
[3, 99, -1, -100] prev = x, curr_idx = 1, count = 4, start = 1
'''