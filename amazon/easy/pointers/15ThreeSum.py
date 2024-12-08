class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def nSum(nums, target, N, result, results):
            if len(nums) < N or N < 2:
                return
                
            # Base case N = 2
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # Skip duplicates
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    # Skip duplicates
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    nSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)   
        
        results = []
        nums.sort()
        nSum(nums, 0, 3, [], results)
        return results