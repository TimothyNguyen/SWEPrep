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
# Python 3 program for the above approach
 
# Function to find the largest area
# when a series of horizontal &
# vertical bars are removed
def largestArea(N, M, H,
                 V, h, v):
 
  # Stores all bars
  s1 = set([])
  s2 = set([])
 
  # Insert horizontal bars
  for i in range(1, N + 2):
    s1.add(i)
 
  # Insert vertictal bars
  for i in range(1, M + 2):
    s2.add(i)
 
  # Remove horizontal separators from s1
  for i in range(h):
    s1.remove(H[i])
 
  # Remove vertical separators from s2
  for i in range( v ):
 
    s2.remove(V[i])
 
  # Stores left out horizontal and
  # vertical separators
  list1 = [0] * len(s1)
  list2 = [0]*len(s2)
 
  i = 0
  for it1 in s1:
    list1[i] = it1
    i += 1
 
  i = 0
  for it2 in s2:
    list2[i] = it2
    i += 1
 
  # Sort both list in
  # ascending order
  list1.sort()
  list2.sort()
 
  maxH = 0
  p1 = 0
  maxV = 0
  p2 = 0
 
  # Find maximum difference of neighbors of list1
  for j in range(len(s1)):
    maxH = max(maxH, list1[j] - p1)
    p1 = list1[j]
 
  # Find max difference of neighbors of list2
  for j in range(len(s2)):
    maxV = max(maxV, list2[j] - p2)
    p2 = list2[j]
 
  # Print largest volume
  print((maxV * maxH))
 
# Driver code
if __name__ == "__main__":
 
  # Given value of N & M
  N = 3
  M = 3
 
  # Given arrays
  H = [2]
  V = [2]
 
  h = len(H)
  v = len(V)
 
  # Function call to find the largest
  # area when a series of horizontal &
  # vertical bars are removed
  largestArea(N, M, H, V, h, v)
 
  # This code is contributed by ukasp.