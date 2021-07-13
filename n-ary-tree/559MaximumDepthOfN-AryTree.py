"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None: return 0
        if len(root.children) == 0: return 1
        
        max_num = 0
        for child in root.children:
            max_num = max(max_num, self.maxDepth(child) + 1)
        return max_num
            