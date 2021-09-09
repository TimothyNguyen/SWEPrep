'''
Given two non-negative integers num1 and num2 repesented as strings,
represented as strings, return the product of num1 and num2, also
represented as a string.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # edge cases
        if len(num1) == 0 or len(num2) == 0: return '0'
        if num1[0] == '0' or num2[0] == '0': return '0'
        res1, res2 = 0, 0
        for d in num1: res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2: res2 = res2 * 10 + (ord(d) - ord('0'))

        # Get the product
        res = res1 * res2

        # Convert to string
        ans = ''
        while res:
            ans = ans + (chr(ord('0')) + chr(res % 10))
            res //= 10
        return ans[::-1]