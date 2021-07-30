class Solution:
    def wordBreak(self, word: str, wordList: List[str]) -> bool:
        wordSet = set(wordList) #O(M)
        dp = [True] + [False] * len(word)
        for i in range(len(word)): # O(N)
            if dp[i]:
                for j in range(i + 1, len(word) + 1): # O(N)
                    if word[i:j] in wordSet: # O(N) String Generation
                        dp[j] = True     
        return dp[-1]
'''
1-2 Sentence Summary
Use a DP Array to check if any substring from i -> j is in the word bank. Build up 
    this solution to the last index of the input string. 

1) Construct a boolean array of size N + 1 as a DP tool
2) Set the first index to True
    - This means there is a valid substring up until that index (exclusive)
3) Iterate from 0 -> N as variable i
    a) If the current index, i, in the DP boolean array is True, we iterate from 
        i -> N as variable j
        i) If the substring input[i:j] is within the word bank, we mark DP[j] as true
            - This signifies the substring of the input from 0 -> j (exlusive) is valid
    b) Continue to build the solution to the end
4) The boolean value of the last index signifies whether the input string can 
    be broken

NOTE: N - Size of Input String, M - Size of Input Word Bank
Time Complexity: O(N^3) [Nested Iteration as well as String Creation]
Space Complexity: O(N) [DP Array of Size N]
'''