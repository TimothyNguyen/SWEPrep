'''
Given an integer array nums, return an integer array counts where 
counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)] # record value and index
        result = [0] * n
        
        def merge_sort(arr, l, r):
            if r - l <= 1:
                return
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m, r)
            merge(arr, l, m, r)
        
        def merge(arr, l, m, r):
            # merge [left, mid) and [mid, right)
            i = l  # current index for the left array
            j = m  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < m and j < r:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - m
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i < m:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - m
                temp.append(arr[i])
                i += 1
            while j < r:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(l, r):
                arr[i] = temp[i - l]
        
        merge_sort(arr, 0, n)
        return result
                