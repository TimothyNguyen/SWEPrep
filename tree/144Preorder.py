# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderRecursiveTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, preorder_list):
            if root is None: return
            preorder_list.append(root.val)
            preorder(root.left, preorder_list)
            preorder(root.right,preorder_list)
        
        preorder_list = []
        preorder(root, preorder_list)
        return preorder_list
        
    def preorderIterativeTraversal(self, root):
        preorder_list = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                preorder_list.append(node.val)
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
        return preorder_list