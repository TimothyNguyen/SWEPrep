class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        left, right = float('inf'), float('inf')
        if root.left: left = self.minDepth(root.left)
        if root.right: right = self.minDepth(root.right)
        return min(left, right) + 1