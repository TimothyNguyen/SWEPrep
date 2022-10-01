'''
You are given an array of integers nums, there is a sliding window of 
size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding 
window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left_arr, right_arr = [0] * n, [0] * n
        left_arr[0], right_arr[n - 1] = nums[0], nums[n-1]

        for i in range(1, n):
            # from left to right
            if i % k == 0:
                left_arr[i] = nums[i]
            else:
                left_arr[i] = max(left_arr[i - 1], nums[i])

            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                right_arr[j] = nums[j]
            else:
                right_arr[j] = max(right_arr[j + 1], nums[j])
        
        output = []
        for i in range(n - k + 1):
            output.append(max(left_arr[i + k - 1], right_arr[i]))
        return output

'''
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
left_arr = [1, 3, 3, -3, -1, 5, 6, 7]
right_arr =[3, 3, -1, 5, 5, 3, 7, 7]
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output