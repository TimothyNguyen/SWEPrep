class Solution:
    def countBits(self, n: int):
        num_bits = 0
        while n:
            num_bits += n & 1
            n >>= 1
        return num_bits