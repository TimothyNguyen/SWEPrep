class Solution:
    def pathSum(self, root, targetSum):
        if root is None:
            return targetSum == 0
        return self.pathSum(root.left, targetSum - root.val) or self.pathSum(root.right, targetSum - root.val)