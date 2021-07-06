# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where each path's sum 
equals targetSum.
A leaf is a node with no children.
'''
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """      
        ans = []
        def helper(root, targetSum, new_list):
            if not root: return
            if not root.left and not root.right and root.val == targetSum:
                ans.append(new_list)
                return
            new_list.append(root.val)
            helper(root.left, targetSum-root.val, new_list)
            helper(root.right, targetSum-root.val, new_list)
        helper(root, targetSum, [])
        return ans
