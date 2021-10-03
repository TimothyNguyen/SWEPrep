'''
Given an m x n binary matrix mat, return the distance of the 
nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        seen = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        lv = 1
        while queue:
            l = len(queue)
            idx = 0
            while idx < l:
                i, j = queue.pop(0)
                for di, dj in dirs:
                    ni = i + di
                    nj= j + dj
                    if 0<=ni<len(mat) and 0<=nj<len(mat[0]) and (ni, nj) not in seen and mat[ni][nj] == 1:
                        mat[ni][nj] = lv
                        queue.append((ni, nj))
                        seen.add((ni, nj))
                idx += 1
            lv += 1
        return mat



