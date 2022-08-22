class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left = [0] * n
        right = [0] * n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j]  = nums[j]
            else:
                right[i] = max(right[j+1], nums[i])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i])) 
        return output