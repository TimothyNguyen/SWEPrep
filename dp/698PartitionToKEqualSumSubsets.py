class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def dfs(parts, nums, idx):
            if idx == len(nums):
                return not sum(parts)
            for i in range(len(parts)):
                if parts[i] >= nums[idx]:
                    parts[i] -= nums[idx]
                    if dfs(parts, nums, idx + 1):
                        return True
                    parts[i] += nums[idx]


        if len(nums) < k or int(sum(nums)/k) != sum(nums) / k:
            return False
        nums.sort(reverse=True)
        parts = [sum(nums)/k] *k
        return self.dfs(parts, nums, 0)

