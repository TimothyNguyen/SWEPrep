# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        def helper(l, r, nums):
            if l > r: return None
            m = l + (r - l)/2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1, nums)
            root.right = helper(m + 1, r, nums)
            return root
        return helper(0, len(nums) - 1, nums)