# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node:
                return [0, 0]
            
            l = helper(node.left)
            r = helper(node.right)
            rob_num = l[1] + r[1] + node.val
            not_rob = max(l) + max(r)
            # print([rob_num, not_rob])
            return [rob_num, not_rob]
        return max(helper(root))