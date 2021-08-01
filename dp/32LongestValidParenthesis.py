class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if (i - dp[i-1]) >= 2 else 0) + 2
                maxans = max(maxans, dp[i])
        return maxans
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(': 
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: maxans = max(maxans, i - stack[-1])
        return maxans
'''