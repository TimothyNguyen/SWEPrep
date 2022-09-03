'''
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        if n == 1:
            return [i for i in range(10)]
        
        def dfs(n, num):
            if n == 0:
                return ans.append(num)
            tail_digit = num % 10
            # using set() to avoid duplicates when k == 0
            next_digits = set([tail_digit + k, tail_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    dfs(n-1, new_num)
        
        for i in range(1, 10):
            dfs(n - 1, i)
        return ans