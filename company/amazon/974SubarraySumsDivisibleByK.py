'''
Given an integer array nums and an integer k, return the number of 
non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
'''
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        array = [0]+k*[0]
        count = 0
        for num in nums:
            count+=num
            remainder = count%k
            array[count%k]+=1
        count = 0
        for ix,remainder in enumerate(array):
            if ix == 0:
                count += remainder*(remainder+1)//2
            else:
                count += remainder*(remainder-1)//2
        return count