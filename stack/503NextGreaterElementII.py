class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []
        for i in range(2 * len(nums) - 1, -1, -1):
            while len(stack) != 0 and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            res[i % len(nums)] = -1 if len(stack) == 0 else nums[stack[-1]]
            stack.append(i % len(nums))
        return res