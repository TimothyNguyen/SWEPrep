class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        numbers = dict()
        for i in range(2, int(n**0.5) + 1):
            if i not in numbers:
                for multiple in range(i*i, n, i):
                    numbers[multiple] = 1
        return n - len(numbers) - 2