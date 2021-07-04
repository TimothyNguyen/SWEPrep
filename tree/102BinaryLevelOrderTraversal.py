# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue, levels = [root], []
        level = 0
        while queue:
            levels.append([])
            size = len(queue)
            for i in range(size):
                root = queue.pop(0)
                levels[level].append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            level += 1
        return levels
        