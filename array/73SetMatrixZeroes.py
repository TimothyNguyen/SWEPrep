class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r_set, c_set = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    r_set.add(r)
                    c_set.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in r_set or c in c_set:
                    matrix[r][c] = 0
    