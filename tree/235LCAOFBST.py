def lca(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> int:    
    n0_val = node0.val
    n1_val = node1.val
    node = root
    while node:
        parent_val = node.val
        if n0_val < parent_val and n1_val < parent_val:
            node = node.left
        elif n0_val > parent_val and n1_val > parent_val: 
            node = node.right
        else:
            break
    return root.val

