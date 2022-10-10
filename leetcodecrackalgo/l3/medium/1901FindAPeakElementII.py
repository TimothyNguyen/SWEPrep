'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent 
neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak
element mat[i][j] and return the length 2 array [i,j].


You may assume that the entire matrix is surrounded by an outer perimeter with the 
value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.


Example 1:

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
'''
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        l, r = 0, m-1
        i = m - 1
        while l <= r:
            m = (l + r) // 2
            if max(mat[m]) > max(mat[r]):
                i = m
                r = m - 1
            else:
                l = m + 1
        return [i, mat[i].index(max(mat[i]))]