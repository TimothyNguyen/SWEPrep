class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i):
            l, r = i, len(nums) - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1

        # First first decreasing element
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        # if i >= 0, then swap
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        # Else reverse
        reverse(i+1)

'''
[2,3,1] -> [3,1,2]
1 <= 3 yes
3 <= 2 no

wrong
[1, 3, 2]
[1, 2, 3]

correct
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
'''
        
# 3281 -> 3821 -> 3812
# 32876 -> 36872 -> 36782
# 32879 -> 32897
# 328886 -> 326888
# 132 -> 231 -> 213
# 151 -> 511
