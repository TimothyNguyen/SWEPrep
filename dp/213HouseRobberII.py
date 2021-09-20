# All house arranged in a circle. Given an integer array nums representing the amount
# of money of each house, return the maximum amount of money you can rob tonight 
# without alerting the police.
class Solution:
    def rob(self, nums) -> int:

        def rob(nums, start, end):
            prevMax, currMax = 0, 0
            for i in range(start, end):
                temp = currMax
                currMax = max(nums[i] + prevMax, currMax)
                prevMax = temp
            return currMax
            
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        max1 = rob(nums, 0, len(nums) - 1)
        max2 = rob(nums, 1, len(nums))
        return max(max1, max2)

soln = Solution()
print(soln.rob([100, 2, 5, 99, 3]))