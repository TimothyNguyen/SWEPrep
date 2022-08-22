class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [float('inf')]*len(nums)
        ans[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                ans[i] = 1
            elif nums[i] > 0:
                val = i + 1
                v = min(ans[val:i+nums[i]+1])
                if v != float('inf'):
                    ans[i] = int(v) + 1
        return ans[0]

        '''
        jumps = 0
            current_jump_end = 0
            farthest = 0
            for i in range(len(nums) - 1):
                # we continuously find the how far we can reach in the current jump
                farthest = max(farthest, i + nums[i])
                # if we have come to the end of the current jump,
                # we need to make another jump
                if i == current_jump_end:
                    jumps += 1
                    current_jump_end = farthest
            return jumps
        '''
            
            
    
'''
[2, 3, 1, 1, 4]
[2, 1, 2, 1, 0]


[2, 3, 0, 1, 4]
[2, 1, inf, 1, 0]
'''