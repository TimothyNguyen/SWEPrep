class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, float('-inf'), float('inf'))
        
    def validate(self, root, l, r):
        if not root:
            return True
        return l < root.val < r and self.validate(root.left, l, root.val) and self.validate(root.right, root.val, r)

    def isValidBSTStack(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, l, u = stack.pop()
            if not root: continue
            val = root.val
            if val <= l or val >= u:
                return False
            stack.append((root.right, val, u))
            stack.append((root.left, l, val))
        return True

    def isValidBSTRecurseInorder(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = float("-inf")
        return inorder(root)
    
    def isValidBSTIterative(self, root: TreeNode) -> bool:
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True