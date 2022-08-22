class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
        return n if k == 1 else -1