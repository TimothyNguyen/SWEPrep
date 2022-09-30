'''
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness 
given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar 
into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other 
pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]

https://leetcode.com/problems/divide-chocolate/solution/

Let nn be the number of chunks in the chocolate and SS be the total sweetness of the chocolate bar.

Time complexity: O(n⋅log(S/(k+1)))

The lower and upper bounds are min(sweetness) and S / (k + 1) respectively. In the worst case 
(when k is small), the right boundary will have the same magnitude as S, and the left boundary
will be 1. Thus, the maximum possible time complexity for a single binary search is O(logS). 
For every single search, we need to traverse the chocolate bar in order to allocate 
chocolate chunks to everyone, which takes O(n) time.

Space complexity: O(1)

For every search, we just need to count the number of people who receive a piece of 
chocolate with enough sweetness, and the total chocolate sweetness for the current 
people, both only cost constant space.
'''
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Initialize the left and right boundaries.
        # left = 1 and right = (total sweetness) / (number of people).
        num_people = k + 1
        l, r = min(sweetness), sum(sweetness) // num_people
        while l < r:
            # Get the middle index between left and right boundary indexes.
            # cur_sweetness stands for the total sweetness for the current person.
            # people_with_chocolate stands for the number of people that have 
            # a piece of chocolate of sweetness greater than or equal to mid.  
            m = (l  + r + 1) // 2
            cur_sweetness = 0
            people_with_chocolate = 0

            # Start assigning chunks to the current person.
            for s in sweetness:
                cur_sweetness += s

                # If the total sweetness is no less than mid, this means we can break off
                # the current piece and move on to assigning chunks to the next person.
                if cur_sweetness >= m:
                    people_with_chocolate += 1
                    cur_sweetness = 0
            
            if people_with_chocolate >= k + 1:
                l = m
            else:
                r = m - 1

        return r
