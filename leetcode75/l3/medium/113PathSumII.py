'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where 
the sum of the node values in the path equals targetSum. Each path should be returned as a 
list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is 
a node with no children.

Time: O(N^2)
Space: O(N)

Time Complexity: O(N^2) where N are the number of nodes in a tree. In the 
worst case, we could have a complete binary tree and if that is the case, then there would 
be N/2 leafs. For every leaf, we perform a potential O(N) operation of copying over the 
pathNodes nodes to a new list to be added to the final pathsList. Hence, the complexity 
in the worst case could be O(N^2).
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def recurseTree(node, remainingSum, pathNodes, pathsList):
            if not node:
                return
            
            # Add current node to path's list
            pathNodes.append(node.val)
            
            if remainingSum == node.val and not node.left and not node.right:
                pathsList.append(list(pathNodes))
            else:
                recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
                recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            pathNodes.pop()
        pathsList = []
        recurseTree(root, targetSum, [], pathsList)
        return pathsList