class Solution:
    def sortColors(self, colors: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, middle, right = 0, 0, len(colors) - 1
        while middle <= right:
            if colors[middle] == 0:
                colors[middle], colors[left] = colors[left], colors[middle] 
                left += 1
                middle += 1
            elif colors[middle] == 1:
                middle += 1
            elif colors[middle] == 2:
                colors[middle], colors[right] = colors[right], colors[middle] 
                right -= 1
                middle += 1
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        idx = 0
        while idx < counts[0]:
            nums[idx] = 0
            print(nums)
            idx += 1
        while idx < counts[0] + counts[1]:
            nums[idx] = 1
            print(nums)
            idx += 1
        while idx < counts[0] + counts[1] + counts[2]:
            nums[idx] = 2
            print(nums)
            idx += 1
'''
