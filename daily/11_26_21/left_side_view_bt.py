'''
Given a Binary Tree, print left view of it. 
Left view of a Binary Tree is set of nodes 
visible when tree is visited from left side.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view_binary_tree(root):
    def dfs(root, ans, level):
        if not root:
            return
        if level == len(ans):
            ans.append(root.val)
        dfs(root.left, ans, level + 1)
        dfs(root.right, ans, level + 1)
    ans = []
    dfs(root, ans, 0)
    return ans

root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
left_view_binary_tree(root)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, ans, level):
            if not root:
                return
            if level == len(ans):
                ans.append(root.val)
            dfs(root.right, ans, level + 1)
            dfs(root.left, ans, level + 1)
        ans = []
        dfs(root, ans, 0)
        return ans