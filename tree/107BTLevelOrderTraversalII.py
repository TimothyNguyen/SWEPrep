class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        return levels[::-1]
        