class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                #if root.val > p.val:
                successor = root
                root = root.left
        return successor
                