from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.maxStack = SortedList()
        self.idxStack = SortedList(key = lambda x: x[1])
        self.idx = 0

    def push(self, x: int) -> None: # O(log N)
        self.maxStack.add((x, self.idx))
        self.idxStack.add((x, self.idx))
        self.idx += 1

        return

    def pop(self) -> int:           # O(log N)
        x, i = self.idxStack.pop(-1)
        self.maxStack.remove((x, i))
        return x

    def popMax(self) -> int:        # O(log N) 
        x, i = self.maxStack.pop(-1)
        self.idxStack.remove((x, i))
        return x

    def top(self) -> int:           # O(1)
        return self.idxStack[-1][0]


    def peekMax(self) -> int:       # O(1)
        return self.maxStack[-1][0]