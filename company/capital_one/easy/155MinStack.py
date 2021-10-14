class MinStack:

    def __init__(self):
        self.s1 = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.min_stack:
            self.min_stack.append(min(val, float('inf')))
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.s1.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()