# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/867956/Python3-Two-solutions-DP-with-Bit-mask(48ms)-DFS%2Bbacktracking-with-detailed-explanations
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or int(sum(nums)/k) != sum(nums)/k: return False #[1]
        N = len(nums)
        nums.sort(reverse=True) #[2]
        
        def dp(mask, cur, memo): # Top-down DP with memoization
            if mask == 0: return cur == 0 #[3]
            elif cur == 0: return dp(mask, sum(nums)/k, memo) #[4]
            if (mask, cur) not in memo:
                res = False
                for bit in range(N): #[5]
                    if mask & (1 << bit): #[6]
                        if nums[bit] > cur: continue # Writing this to be more explicit, for easy-understanding
                        if dp(mask ^ (1 << bit), cur-nums[bit], memo): #[7]
                            res = True
                            break
                memo[(mask, cur)] = res
            return memo[(mask, cur)] 
        return dp(2**N-1, sum(nums)/k, dict()) #[8]