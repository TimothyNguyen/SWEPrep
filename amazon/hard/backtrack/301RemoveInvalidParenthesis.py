'''
Given a string s that contains parentheses 
and letters, remove the minimum number of 
invalid parentheses to make the input string 
valid.

Return all the possible results. You may return the 
answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

O(2^n) time
O(n) space
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def backtrack():
            pass
        for ch in s:
            