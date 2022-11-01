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
        res = []
        self.max_ans = 0
        
        if not s: return res
        def dfs(left_word, right_word, count_left, max_left):
            if len(left_word) == 0:
                if count_left == 0 and len(right_word) != 0:
                    if max_left > self.max_ans:
                        self.max_ans = max_left
                    if max_left == self.max_ans and right_word not in res:
                        res.append(right_word)
                return
        
            if left_word[0] == '(':
                dfs(left_word[1:], right_word + "(", count_left + 1, max_left + 1)
                dfs(left_word[1:], right_word, count_left, max_left)
            elif left_word[0] == ')':
                if count_left > 0:
                    dfs(left_word[1:], right_word + ")", count_left - 1, max_left)
                dfs(left_word[1:], right_word, count_left, max_left)
            else:
                dfs(left_word[1:], right_word + left_word[0], count_left, max_left)
        
        dfs(s, "", 0, 0)
        if len(res) == 0:
            res.append("")
        return res