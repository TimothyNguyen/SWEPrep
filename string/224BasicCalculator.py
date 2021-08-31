class Solution:
    self.i = 0

    def calculate(self, s: str) -> int:

        def cal(num: int, tmp: int, op: int) -> int:
            if op == '+': return num + tmp
            elif op == '-': return num - tmp
            elif op == '*': return num * tmp
            return num / tmp

        if not s or len(s) == 0: return 0
        result = tmp = num = 0
        op = '+'
        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit(): tmp = (tmp * 10) + int(ch)
            elif ch == '(': tmp = self.calculate(s)
            elif ch == ')': break
            elif ch != ' ':
                num = cal(num, tmp, op)
                if ch == '+' or ch == '-':
                    result += num
                    num = 0
                # result tmp and op for next char processed
                tmp = 0
                op = ch