class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = [0] * len(s) 
        dp[0] = 1
        
         
        idxes = [(-1, -1)] * 26 # Track first & second idx
        idxes[ord(s[0]) - ord('A')] = (-1, 0)
        
        # [a, b, c]
        # [1, 3, 6]
        
        for i in range(1, len(s)):
            first_idx, second_idx = idxes[ord(s[i]) - ord('A')]
            dp[i] = dp[i-1] + (i - second_idx) - (second_idx - first_idx)
            idxes[ord(s[i]) - ord('A')] = (second_idx, i)
            # print(dp)
        return sum(dp)