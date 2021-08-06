class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # edge cases 
        if len(num1) == 0 or len(num2) == 0: return '0'
        if num1[0] == '0' or num2[0] == '0': return '0'
        # convert to integer
        res1, res2 = 0, 0
        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        
        # Get product result
        res = res1 + res2

        # convert back to string
        ans = ''
        while res:
            ans = ans + chr(ord('0') + res % 10)
            res //= 10
        return ans[::-1]