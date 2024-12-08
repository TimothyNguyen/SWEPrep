class MinStack:

    def __init__(self):
        self.s : List[int] = []
        self.min_s : List[int] = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min_s) == 0 or val <= self.min_s[-1]:
            self.min_s.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if self.min_s[-1] == val:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()