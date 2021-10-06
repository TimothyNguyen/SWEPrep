class Solution:
    def mySqrt(self, x: int) -> int:
        def sqrt_helper(l, r, target):
            if r - l <= 1: return l
            
            m = (l + r) // 2
            mid_num = m * m
            if target == mid_num: 
                return m
            elif target < mid_num:
                return sqrt_helper(l, m, target)
            else:
                return sqrt_helper(m, r, target)
            # return l
            
        if x == 0 or x == 1: return x
        return sqrt_helper(0, x, x)