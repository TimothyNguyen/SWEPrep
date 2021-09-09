'''
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest 
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

- Why does this work? What's the intuition 
'''
def nextPermutation(self, nums: List[int]) -> None:

    def reverse(nums: List[int], start: int):
        i, j = start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    i = len(nums) - 2

    # First find the first decreasing element
    while i >= 0 and nums[i + 1] <= nums[i]: i -= 1

    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]: j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    reverse(nums, i + 1)