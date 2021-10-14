class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ans = []
        if len(nums) == 0:
            return ans
        
        i = 0
        ans.append(str(nums[0]))
        for j in range(1, len(nums)):
            if nums[j - 1] + 1 != nums[j]:
                if j - 1 > i:
                    ans[-1] += '->' + str(nums[j-1]) 
                i = j
                ans.append(str(nums[j]))
            if j == len(nums) - 1 and i != j:
                ans[-1] += '->' + str(nums[j]) 
        return ans
            