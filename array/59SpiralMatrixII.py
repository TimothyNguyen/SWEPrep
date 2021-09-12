class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        soln = [[0] * n for _ in range(n)] 
        r1, c1, r2, c2 = 0, 0, n - 1, n - 1
        i = 1
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                soln[r1][c] = i
                i += 1
            for r in range(r1 + 1, r2 + 1):
                soln[r][c2] = i
                i += 1
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    soln[r2][c] = i
                    i += 1
                for r in range(r2, r1, -1):
                    soln[r][c1] = i
                    i += 1
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return soln