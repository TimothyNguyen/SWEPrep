'''
Given a string s, partition s such that every substring of the partition 
is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
'''
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[-1*(len(s)+1)]*(len(s)+1)]
        ans = []
        def is_palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
        def dfs(curr, s):
            if s == "":
                ans.append(curr)
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    dfs(curr + [s[:i + 1]], s[i + 1:])
        dfs([], s)
        return ans
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        def isPalindrome(st):
            return st == st[::-1]
        
        def dfs(curr=[], index=1):
            if index == len(s) + 1:
                out.append(list(curr))
                return
            for i in range(index, len(s)+1):
                #print(s[index-1:i])
                if isPalindrome(s[index-1:i]):
                    #print("yes" + s[index-1:i])
                    curr.append(s[index-1:i])
                    dfs(curr, i+1)
                    curr.pop()
        dfs()
        return out