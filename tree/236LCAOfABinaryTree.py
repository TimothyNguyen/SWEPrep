# Given te lca
import collections
ans = None
def lca(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
    
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(current_node):
        if not root: return False # return Status(num_target_nodes=0 , ancestor=None)

        left = lca_helper(current_node.left)
        right = lca_helper(current_node.right)

        mid = current_node == node0 or current_node == node1

        # if any two of the three flags become true
        if mid + left + right >= 2:
            ans = current_node
        
        return mid or left or right
    lca_helper(root)
    return ans
        


