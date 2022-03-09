'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            min_ans = nums[i]
            max_ans = nums[i]
            for j in range(i + 1, len(nums)):
                max_ans = max(max_ans, nums[j])
                min_ans = min(min_ans, nums[j])
                res += (max_ans - min_ans)
        return res
'''
'''
The idea is to use 2 monotonic stacks to find the number of subarrays a particular element 
is a max or min for and calculate its contribution to the total max or min sum, since 
we are asked to find the diff between ALL of the ranges and doesn't matter in which order we sum them.
The answer can then be found as TOTAL_SUM(all_max_subsums) - TOTAL_SUM (all_min_subsums).
'''
class Solution:
    def process_stack(self, nums, cur_idx, stack, compare_op, prefix, suffix):
        '''
        Process the monotonic stack used to find the boundaries of subarrays the current value is min or max for.
        '''
        while stack and compare_op(nums[stack[-1]], nums[cur_idx]):
            suffix[stack.pop()] = cur_idx
            
        prefix[cur_idx] = stack[-1] if stack else -1
        stack.append(cur_idx)
        
    def count_presum(self, nums, i, prefix, suffix):
        '''
        Count the subarrays a particular value is a min or max for (using corresponding prefix and suffix arrays to find this value)
        and calculate its total contribution to the final result.
        '''
        left = i - prefix[i]
        right = suffix[i] - i
        return left * right * nums[i]
            
    def subArrayRanges(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError()
            
        n = len(nums)
        res = 0
        
        suffix_min, suffix_max = [n] * n, [n] * n
        prefix_min, prefix_max = [0] * n, [0] * n
        stack_min, stack_max = [], []
        
        for i in range(n):
            self.process_stack(nums, i, stack_min, operator.ge, prefix_min, suffix_min)
            self.process_stack(nums, i, stack_max, operator.le, prefix_max, suffix_max)

        for i in range(n): 
            res +=  self.count_presum(nums, i, prefix_max, suffix_max) - self.count_presum(nums, i, prefix_min, suffix_min)
                
        return res

