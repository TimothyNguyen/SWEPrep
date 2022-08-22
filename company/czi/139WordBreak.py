'''
Given a string s and a dictionary of strings 
wordDict, return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    def wordBreak(s: str, wordDict: List[str]):
        queue = [0]
        visited = [0]*len(s)
        hashset = set(wordDict)
        while queue:
            start = queue.pop(0)
            visited[start] = 0
            if visited[start] == 0:
                for i in range(start + 1, len(s) + 1):
                    if s[start:i] in hashset:
                        queue.append(i)
                        if i == len(s): return True
                visited[start] = 1
        return False