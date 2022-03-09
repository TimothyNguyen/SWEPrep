class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = 0
        flip = 0
        for i in range(len(s)):
            if s[i] == '1':
                one += 1
            else:
                flip += 1
            flip = min(flip, one)
        return flip