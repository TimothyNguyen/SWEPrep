# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getLargest(node):
    while node and node.right: 
        node = node.right
    return node

def getSecondLargest(node):
    if not node.right and node.left: return getLargest(node.left)
    if node.right and not node.left and not node.right: return node
    return getSecondLargest(node.right)