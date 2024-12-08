# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) <= 0:
            return None
        m = len(nums) // 2
        root_node = TreeNode(nums[m])
        l, r = m, m + 1
        root_node.left = self.sortedArrayToBST(nums[:l])
        root_node.right = self.sortedArrayToBST(nums[r:])
        return root_node
