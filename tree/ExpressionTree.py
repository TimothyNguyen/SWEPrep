class Et:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'

def inorder(t):
    if t:
        inorder(t.left)
        print(t.value)
        inorder(t.right)

# Returns root of constructed tree for
# given postfix expression
def constructTree(postfix):
    stack = []

    # Traverse through every char of input expression
    for char in postfix:
        # if operand, simply push into stack
        if not isOperator(char):
            t = Et(char)
            stack.append(t)
        else:
            # pop two top nodes
            t = Et(char)
            t1 = stack.pop()
            t2 = stack.pop()

            # make them children
            t.right = t1
            t.left = t2
        
            # Add this subexpression to stack
            stack.append(t)
    t = stack.pop()
    return t

# Driver program to test above
postfix = "ab+ef*g*-"
r = constructTree(postfix)
print("Infix expression is", inorder(r))