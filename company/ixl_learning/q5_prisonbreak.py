'''
Programmer Sam is planning to escape from prison! The prison's gate consists 
of horizontal and vertical bars that are spaced one unit apart, so the area 
of each hole between the bars is 1 × 1. Sam manages to remove certain bars 
and make some of these holes bigger. Determine the area of the largest hole 
in the gate after the bars are removed.

For example, consider the diagram below. The left image depicts the initial
prison gate with n = 6 horizontal and m = 6 vertical bars, where the area of 
the biggest hole in the bars is 1 × 1. The right image depicts that same gate 
after Sam removes horizontal bar 4 and vertical bar 2, at which point the 
area of the biggest hole in the bars becomes 2 × 2 = 4:

Function Description Complete the function prison in the editor below. 
The function must return a long integer denoting the area of the biggest 
hole in the prison gate's bars.
'''

# Input: N = 3, M = 3, H[] = {2}, V[] = {2}
# Output: 4

'''
Approach: Follow the steps below to solve the problem:

Initialize two sets, s1 & s2 to store the integers.
Iterate over the range [1, N+1] and store every integer in s1.
Similarly, iterate over the range [1, M + 1] and store every integer in s2.
Traverse the array H[] and remove all H[i] from s1.
Similarly, traverse the array V[] and remove all V[i] from s2.
Convert updated s1 and s2 sets into lists l1 and l2.
Sort both the lists in ascending order.
Traverse the list l1 and l2 and store the maximum distance between two neighbours as maxH and maxV respectively.
Print the product of maxH and maxV as the largest area.
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Start by sorting the inputs
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Consider the edges first
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            # horizontalCuts[i] - horizontalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible height
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
        
        # Consider the edges first
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            # verticalCuts[i] - verticalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible width
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])
        
        # Python doesn't need to worry about overflow - don't forget the modulo though!
        return (max_height * max_width) % (10**9 + 7)