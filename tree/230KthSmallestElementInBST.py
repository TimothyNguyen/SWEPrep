class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder_list = []
        def inorder(root):
            if root is None or len(inorder_list) >= k: return
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return inorder_list[k-1]
            
        