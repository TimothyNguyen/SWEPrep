class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        num = self.myPow(x, int(n / 2))
        if n % 2 == 0:
            return num ** 2
        elif n > 0:
            return num * num * x
        return (num * num) / x
'''
10
5
2.5
'''