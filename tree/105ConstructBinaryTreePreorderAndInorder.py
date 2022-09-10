# - Build a hashmap to record the relation of value -> index for inorder, so that we can find the position of root in constant time.
# - Initialize an integer variable preorderIndex to keep track of the element that will be used to construct the root.
# Implement the recursion function arrayToTree which takes a range of inorder and returns the constructed binary tree:
#   if the range is empty, return null;
#   initialize the root with preorder[preorderIndex] and then increment preorderIndex;
#   recursively use the left and right portions of inorder to construct the left and right subtrees.
# Time/Space: O(N)

# The two key observations are:
# 1. Preorder traversal follows Root -> Left -> Right, therefore, given 
# the preorder array preorder, we have easy access to the root which is preorder[0].
# 2. Inorder traversal follows Left -> Root -> Right, therefore if we 
# know the position of Root, we can recursively split the entire 
# array into two subtrees.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right:
                return None
            
            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            
            preorder_index += 1
            
            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            
            return root
        
        preorder_index = 0
        
        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for idx, val in enumerate(inorder):
            inorder_index_map[val] = idx
            
        return array_to_tree(0, len(preorder) - 1)