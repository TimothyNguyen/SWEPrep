'''
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''
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

'''
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
'''

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
    