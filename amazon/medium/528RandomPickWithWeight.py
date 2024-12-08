import math


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
    
    def pickIndex(self) -> int:
        weight = self.total_sum * math.rand()
        l, r = 0, len(self.prefix_sums)
        while l <= r:
            m = (l + r) // 2
            if weight > self.prefix_sums[m]:
                l = m + 1
            else:
                r = m - 1
        return l