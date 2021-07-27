class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return 1
        a, b, c = 1, 1, None
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return c