# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return symmetric(left.left, right.right) and symmetric(left.right, right.left)
        
        if not root:
            return True
        return symmetric(root.left, root.right)
        
        
        