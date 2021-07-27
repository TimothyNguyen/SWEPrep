class Solution:
    def minPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)): 
            matrix[i][0] += matrix[i-1][0]
        for j in range(1, len(matrix[0])):
            matrix[0][j] += matrix[0][j-1]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
        return matrix[len(matrix)-1][len(matrix[0]) - 1]
                