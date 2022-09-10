'''
A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them. A node can only appear 
in the sequence at most once. Note that the path does not need to pass 
through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Time: O(N)
Space: O(H)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_ans = -float('inf')
        def dfs(root):
            m = root.val
            l = dfs(root.left) if root.left else 0
            r = dfs(root.right) if root.right else 0    
            curr_max_num = max(max(m + l + r, m + r), max(m + l, m))
            self.max_ans = max(self.max_ans, curr_max_num)
            return max(max(m + l, m + r), m)
        if not root:
            return 0
        dfs(root)
        return self.max_ans