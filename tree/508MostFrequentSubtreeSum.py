# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elementsSeen = dict()
        def dfs(node):
            if node == None: return 0
            left, right = dfs(node.left), dfs(node.right)
            value = left + right + node.val
            if value not in elementsSeen: 
                elementsSeen[value] = 0
            elementsSeen[value] += 1
            return value
        dfs(root)
        
        max_val = max(elementsSeen.values())
        maxis = [k for k, v in elementsSeen.items() if v == max_val]
        return maxis
        