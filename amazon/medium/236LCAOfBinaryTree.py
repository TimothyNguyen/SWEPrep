# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        if p == q:
            return p
        def dfs(curr_node: 'TreeNode'):
            if not curr_node:
                return False
            l = dfs(curr_node.left)
            r = dfs(curr_node.right)
            m = curr_node == p or curr_node == q
            if m + l + r >= 2:
                self.ans = curr_node
            return l or m or r
        dfs(root)
        return self.ans