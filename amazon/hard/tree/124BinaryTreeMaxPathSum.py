from typing import Optional


class TreeNode:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r
    
class Solution:
    def maxPathSum(self, root : Optional[TreeNode]) -> int:
        max_val = -float('inf')
        def dfs(node : Optional[TreeNode]):
            if not node:
                return 0
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            left_subtree_with_center_val = node.val + left_node.val
            all_vals = node.val + left_node.val + right_node.val
            right_subtree_with_center_val = node.val + right_node.val 
            center_node_val = node.val
            subtree_to_include_vals = max(left_subtree_with_center_val, right_subtree_with_center_val, center_node_val)
            max_val = max(max_val, all_vals, max(subtree_to_include_vals))
            return subtree_to_include_vals
        dfs(root)
        return max_val