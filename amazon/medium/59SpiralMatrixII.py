class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r1, c1 = 0, 0
        r2, c2 = n - 1, n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                matrix[r1][c] = count
                count += 1
            for i in range(r1 + 1, r2 + 1):
                matrix[i][c2] = count
                count += 1
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1-1, -1):
                    matrix[r2][c] = count
                    count += 1
                for r in range(r2-1, r1, -1):
                    matrix[r][c1] = count
                    count += 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return matrix