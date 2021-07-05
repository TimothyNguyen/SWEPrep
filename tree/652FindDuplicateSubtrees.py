# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time + space
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans = []
        mapping = {}
        def dfs(node, path):
            if node:
                path += str(node.val) + "-" + dfs(node.left, path) + "-" + dfs(node.right, path)
                if path in mapping:
                    mapping[path] += 1
                    if mapping[path] == 1: 
                        ans.append(node)
                else: 
                    mapping[path] = 0
                return path
            else: return "#"
        dfs(root, "")
        return ans
        
        