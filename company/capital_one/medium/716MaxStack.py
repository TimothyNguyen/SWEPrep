class MaxStack:

    def __init__(self):
        self.s1 = []
        self.max_stack = []

    def push(self, val: int) -> None:
        max_num = val if len(self.max_stack) == 0 or val >= self.max_stack[-1] else self.max_stack[-1]
        self.s1.append(val)
        self.max_stack.append(max_num)

    def pop(self) -> int:
        val = self.s1.pop()
        self.max_stack.pop()
        return val

    def top(self) -> int:
        return self.s1[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_num = self.peekMax()
        temp_stack = []
        while self.top() != max_num:
            temp_stack.append(self.pop())
        self.pop()
        while len(temp_stack) > 0:
            self.push(temp_stack.pop())
        return max_num
    