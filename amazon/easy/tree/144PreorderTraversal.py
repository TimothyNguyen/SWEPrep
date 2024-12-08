# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: Optional[TreeNode]):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        ans = []
        preorder(root)
        return ans
    
    def preorderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        while True:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            root = stack.pop()
            root = root.right