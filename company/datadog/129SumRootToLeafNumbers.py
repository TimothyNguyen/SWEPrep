'''
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = 0
        def preorder(root, value):
            if root is None: return
            if root.left is None and root.right is None: 
                self.answer += value * 10 + root.val
                return
            if root.left: preorder(root.left, value * 10 + root.val)
            if root.right: preorder(root.right, value * 10 + root.val)
        preorder(root, 0)
        return self.answer
        