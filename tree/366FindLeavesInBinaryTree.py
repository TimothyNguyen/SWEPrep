# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = dict()
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            level = max(left, right) + 1
            if level not in ans: 
                ans[level] = []
            ans[level].append(root.val)
            return level
        dfs(root)
        output = []
        for k in ans:
            output.append(ans[k])
        return output