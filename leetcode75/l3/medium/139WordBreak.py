'''
Given a string s and a dictionary of strings wordDict, return 
true if s can be segmented into a space-separated sequence of 
one or more dictionary words.

Note that the same word in the dictionary may be reused multiple 
times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Time:O(len(s^2))
Space: O(S)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = [0]
        visited = [0] * len(s)
        wordSet = set(wordDict)
        while queue:
            start = queue.pop()
            if visited[start] == 0:
                for i in range(start + 1, len(s) + 1):
                    if s[start:i] in wordSet:
                        queue.append(i)
                        if len(s) == i: return True
                visited[start] = 1
        return False