'''
Given the root of a binary tree, return the same tree where every subtree 
(of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            if not left:
                root.left = None
            if not right:
                root.right = None
            if root.val == 0 and not left and not right:
                return False
            return True
        
        dummy_root = TreeNode(0, root)
        res = dfs(dummy_root)
        if not res:
            return None
        return root