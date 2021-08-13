class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsetSet = set()
        def backtrack(idx, curr):
            # If the combination is done
            if len(curr) == k and ''.join(str(curr)) not in subsetSet: 
                output.append(list(curr))
                subsetSet.add(''.join(str(curr)))
                return
            for i in range(idx, len(nums)):
                # Add nums[i] into the current combo
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        nums.sort()
        output = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
        return output