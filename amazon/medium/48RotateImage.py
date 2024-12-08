class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        # Reflect        
        n1, n2 = 0, len(matrix[0]) - 1
        while n1 < n2:
            for r in range(len(matrix)):
                temp = matrix[r][n1]
                matrix[r][n1] = matrix[r][n2]
                matrix[r][n2] = temp
            n1 += 1
            n2 -= 1
        return matrix