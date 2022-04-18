# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count, k = 0, sum
        h = defaultdict(int)
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            
            # Get current prefix sum
            curr_sum += node.val

            # Find sum
            if curr_sum == k:
                count += 1
            
            count += h[curr_sum - k]
            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1


        preorder(root, 0)
        return count
# O(n) time  + space