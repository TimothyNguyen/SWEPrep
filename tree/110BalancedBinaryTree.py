class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root):
        if not root: return -1
        return 1 + max(self.height(root.left), self.height(root.right))