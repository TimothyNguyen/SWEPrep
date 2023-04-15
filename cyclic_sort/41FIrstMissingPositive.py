class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            # check if positive, in range, and not in correct position
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp
            else: 
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

        # n = len(nums)

        # if 1 not in nums:
        #     return 1

        # # Replace negative numbers, zeros, and numbers larger than n by 1s.
        # for i in range(n):
        #     if nums[i] <= 0 or nums[i] > n:
        #         nums[i] = 1

        # # Use index as a has key and number sign as a presence detector.
        # # For example, if nums[1] is negative that means that number `1`
        # # is present in the array. If nums[2] is positive - number 2 is missing
        # for i in range(n):
        #     a = abs(nums[i])
        #     # If you meet number a in the array - change 
        #     # the sign of a-th element.
        #     # Be careful with duplicates : do it only once.
        #     if a == n:
        #         nums[0] = -abs(nums[0])
        #     else:
        #         nums[a] = -abs(nums[a])

        # # now the index of the 1st positive number is equal to the 
        # # first missing positive
        # for i in range(1, n):
        #     if nums[i] > 0:
        #         return i
            
        # if nums[0] > 0:
        #     return n
        
        # return n + 1