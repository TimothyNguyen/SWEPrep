class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif (ch == ')' or ch == '}' or ch == ']') and len(stack) == 0:
                return False
            elif (ch == ')' and stack[-1] != '(') or (ch == '}' and stack[-1] != '{') or (ch == ']' and stack[-1] != '[') :
                return False
            else:
                stack.pop()
        return len(stack) == 0
                                        
                