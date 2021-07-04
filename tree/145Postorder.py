class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder, stack = [], [root]
        while stack:
            root = stack.pop()
            if root:
                postorder.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        return postorder[::-1]
    
    def postorderRecursive(self, root):
        output = []
        def postorder(root):
            if not root: return
            postorder(root.left)
            postorder(root.right)
            output.append(root.val)
        postorder(root)
        return output