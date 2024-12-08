class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' and len(stack) >= 2:
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 + s2)
            elif token == '-' and len(stack) >= 2:
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 - s2)
            elif token == '*' and len(stack) >= 2:
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 * s2)
            elif token == '/' and len(stack) >= 2:
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(s1 / s2))
            else:
                stack.append(int(token))
        return stack[0]