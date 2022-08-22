# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        def lca_helper(curr):
            nonlocal ans
            if not curr:
                return False
            
            left = lca_helper(curr.left)
            right = lca_helper(curr.right)
            mid = curr == p or curr == q
            if mid + left + right >= 2:
                ans = curr
            return mid or left or right
        
        lca_helper(root)
        return ans