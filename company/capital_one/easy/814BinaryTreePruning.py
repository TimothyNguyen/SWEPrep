# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            if not left:
                root.left = None
            if not right:
                root.right = None
            if root.val == 0 and not left and not right:
                return False
            return True
        
        dummy_root = TreeNode(0, root)
        res = dfs(dummy_root)
        if not res:
            return None
        return root
                