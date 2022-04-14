'''
Given a sorted integer array arr, two integers k and x, return the 
k closest integers to x in the array. The result should also be 
sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Input: arr = [1,2,3,4,5], k = 4, x = 3

Time complexity: O(log(N)+k).

The initial binary search to find where we should start our window 
costs O(log(N)). Our sliding window initially starts with size 
0 and we expand it one by one until it is of size k, thus it costs 
O(k) to expand the window.

Space complexity: O(1)
'''
from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case 
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        # return the window
        return arr[left + 1:right]