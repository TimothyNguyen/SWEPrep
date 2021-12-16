'''
Write a Program that takes two strings and computes the minimum number of edits needed to
transform the first string into the second string.
Hint: Consider the same problem for prefixes of the two strings.
'''

class Solution:
    def levenhshtein_distance(self, word1: str, word2: str):
        n, m = len(word1), len(word2)
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        dp = [ [0] * (m + 1) for _ in range(n + 1)]
        