# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.stack.append(root.val)
            inorder(root.right)
        inorder(root)
        self.stack = self.stack[::-1]
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop() if self.hasNext() else None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()