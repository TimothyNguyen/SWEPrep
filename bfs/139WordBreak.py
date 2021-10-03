class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue, visited = [0],  len(s) * [0]
        hashset = set(wordDict)
        while queue:
            start = queue.pop(0)
            if visited[start] == 0:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in hashset:
                        queue.append(end)
                        if end == len(s): return True
                visited[start] = 1
        return False

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordSet:
                        dp[j] = True
                        print(dp)
        return dp[-1]


Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused
multiple times in the segmentation.
'''