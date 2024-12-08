# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans
    
    def inorderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            root = stack.pop()
            ans.append(root.val)
            root = root.right
