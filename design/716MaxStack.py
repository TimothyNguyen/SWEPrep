class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        max_num = x if not self.s2 else self.s2[-1]
        self.s2.append(max_num if max_num > x else x)
        self.s1.append(x)

    def pop(self) -> int:
        self.s2.pop()
        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def peekMax(self) -> int:
        return self.s2[-1]

    def popMax(self) -> int:
        max_num = self.peekMax()
        buffer = []
        while self.top() != max_num:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()