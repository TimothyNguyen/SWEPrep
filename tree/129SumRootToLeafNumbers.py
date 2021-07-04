# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    answer = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root, value):
            if root is None: return
            if root.left is None and root.right is None: 
                self.answer += value * 10 + root.val
                return
            if root.left: preorder(root.left, value * 10 + root.val)
            if root.right: preorder(root.right, value * 10 + root.val)
        preorder(root, 0)
        return self.answer
        