class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_bracket_set = set(['(', '{', '['])
        right_bracket_set = set([')', '}', ']'])
        for i in range(len(s)):
            if s[i] in left_bracket_set:
                stack.append(s[i])
            else:
                if len(stack) == 0 or (s[i] == ')' and stack[-1] != '(') or (s[i] == '}' and stack[-1] != '{') or (s[i] == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return len(stack) == 0