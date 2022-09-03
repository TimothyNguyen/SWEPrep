# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def  array_to_tree(left, right):
            if left > right:
                return None
            
            # pick up the last element as root
            val = postorder.pop()
            root = TreeNode(val)
            
            # build right subtree
            root.right = array_to_tree(inorder_index_map[val] + 1, right)
            root.left = array_to_tree(left, inorder_index_map[val] - 1)
            return root;
        
        # build a hashmap value -> its index
        inorder_index_map = {}
        for idx, val in enumerate(inorder):
            inorder_index_map[val] = idx
        
        return array_to_tree(0, len(inorder) - 1)