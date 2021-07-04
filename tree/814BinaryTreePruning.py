# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root: return 0
            # if not root.left and not root.right: return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0: root.left = None
            if right == 0: root.right = None
            return max(root.val, max(left, right))
        return root if dfs(root) else None