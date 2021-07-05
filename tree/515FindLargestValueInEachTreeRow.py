# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue, levels = [root], []
        while queue:
            maxnum = float("-inf")
            size = len(queue)
            for i in range(size):
                root = queue.pop(0)
                if root.val > maxnum:
                    maxnum = root.val
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            levels.append(maxnum)
        return levels
        