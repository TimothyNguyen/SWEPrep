class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr):
            # If the combination is done
            if len(curr) == k: 
                output.append(list(curr))
                return
            for i in range(idx, len(nums)):
                # Add nums[i] into the current combo
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
        return output

