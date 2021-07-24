class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        return self.sqrt_helper(0, x, x)

    def sqrt_helper(self, l, r, target):
        if r - l <= 1: return l

        m = (l + r) // 2
        mid_squared = m * m
        if mid_squared == target:
            return m
        elif mid_squared > target:
            return self.sqrt_helper(l, m, target)
        else:
            return self.sqrt_helper(m, r, target)
            