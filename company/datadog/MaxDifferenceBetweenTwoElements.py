'''
Given an array arr[] of integers, find out the maximum difference 
between any two elements such that larger element appears after 
the smaller number. 

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
'''
def highest_mountain_peak(arr):
    ans = 0
    smallest_num = float('inf')
    for i in range(len(arr)):
        ans = max(ans, arr[i] - smallest_num)
        smallest_num = min(smallest_num, arr[i])
    return ans
