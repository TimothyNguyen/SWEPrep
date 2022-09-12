'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least 
one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Time complexity : (n * log(m)). Heapification of m elements requires O(log(m) time. This step could be done for all 
the elements of the given lists in the worst case. Here, n refers to the total number of elements in all the lists. 
m refers to the total number of lists.
Space complexity : O(m). nextnextnext array of size m is used. A Min-Heap with m elements is also used.
'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # store the first element in each list in a min heap
        # we need to store the number, corresponding row for that number, 
        # and index in row for that number
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        
        # Best interval so far with the minimum set to negative infinity 
        # and the maximum set to positive infinity
        best_interval = (float("-inf"), float("inf")) 

        # go through all the rows to get the current highest number
        curr_max = max(row[0] for row in nums) 
        
        while heap:
            # Remove next smallest element in heap
            curr_min, row_num, row_idx = heapq.heappop(heap)
            
            if curr_max - curr_min < best_interval[1] - best_interval[0]:
                best_interval = (curr_min, curr_max)
            
            if row_idx + 1 == len(nums[row_num]):
                return best_interval
            
            new_elem = nums[row_num][row_idx + 1]
            curr_max = max(curr_max, new_elem)
            heapq.heappush(heap, (new_elem, row_num, row_idx+1))