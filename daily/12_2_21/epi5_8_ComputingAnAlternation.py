'''
Write a program that takes an array A of n numbers, and rearranges A's elements 
to get a new array B having the property that
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ....

1. Naive solution - sort array and interleave the bottom and top halves of sorted array
OR sort and swap elements at the pairs - O(n lg n)
'''
def rearrange(A):
    A.sort()
    for i in range(0, len(A), 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A
'''
Better solution - O(n)
- swap A[i] and A[i + 1] when
1. i is even and A[i] > A[i+1] OR 
2. i is odd and A[i] < A[i + 1] 
'''
def better_soln(A):
    for i in range(len(A)):
        if (i % 2 == 0 and A[i] > A[i + 1]) or (i % 2 != 0 and A[i] < A[i + 1]):
            A[i], A[i+1] = A[i+1], A[i]
    return A