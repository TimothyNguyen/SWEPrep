class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s: List[int] = list()
        for c in tokens:
            val = self.compute(s.pop(), s.pop(), c) if self.isOperator(c) else c
            s.append(int(val))
        return s.pop()


    # Helper Func
    def compute(self, n1, n2, operator):
        if operator == "+":
            return n2 + n1
        elif operator == "-":
            return n2 - n1
        elif operator == "*":
            return n2 * n1
        else:
            return n2 / n1

    # Helper Func
    def isOperator(self, c):
        return c == "+" or c == "-" or c == "*" or c == "/"