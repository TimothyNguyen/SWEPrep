'''
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., 
numsr-1, numsr] of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
                
        res = []
        backtrack()
        return res