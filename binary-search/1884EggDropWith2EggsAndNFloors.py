class Solution:
    def twoEggDrop(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            mid_num = (m * (m + 1)) // 2
            if mid_num >= n:
                r = m - 1
            else:
                l = m + 1
        return l