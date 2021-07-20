class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0 and c > 0 and matrix[r-1][c-1] != matrix[r][c]:
                    return False
        return True