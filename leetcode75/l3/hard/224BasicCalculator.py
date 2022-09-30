class Solution:
    
    def __init__(self):
        self.i = 0
        
    def calculate(self, s: str) -> int:        
        
        if s == None or len(s) == 0: return 0
        op = '+'
        result, tmp, num = 0, 0, 0
        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit(): 
                tmp = tmp * 10 + int(ch)
            elif ch == '(':
                tmp = self.calculate(s)
            elif ch == ')':
                break
            elif ch != ' ':
                num = self.cal(num, tmp, op)
                if ch == '+' or ch == '-':
                    result += num
                    num = 0
                tmp = 0
                op = ch
        # self.i = 0
        e =  self.cal(num, tmp, op)
        return result + e
    
    def cal(self, num, tmp, op):
        if op == '+': return num + tmp
        elif op == '-': return num - tmp
        elif op == '*': return num * tmp
        else: return int(num / tmp)
    
    
            