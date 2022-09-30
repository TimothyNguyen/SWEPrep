'''
Given the availability time slots arrays slots1 and slots2 of two people and 
a meeting duration duration, return the earliest time slot that works for both 
of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an 
inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with 
each other. That is, for any two time slots [start1, end1] and [start2, end2] of 
the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Time complexity: O((M+N)log(M+N)), when M is the length of slots1 and N is the length of slots2.
Space complexity: O(M+N). This is because we store all M+N time slots in a heap
'''
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)
        
        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []
