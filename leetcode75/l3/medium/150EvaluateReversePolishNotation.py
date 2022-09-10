'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or len(tokens) == 0: return 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                total = num1 + num2 if tokens[i] == '+' else num1 - num2
                stack.append(total)
            elif tokens[i] == '*' or tokens[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                total = num1 * num2 if tokens[i] == '*' else int(num1 / num2)
                stack.append(total)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()