'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes 
(the leftmost and rightmost non-null nodes), where the null nodes between 
the end-nodes that would be present in a complete binary tree extending
down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Time/Space: O(N) -> N = # nodes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))
            # Calculate the length of curr level
            max_width = max(max_width, col_index - level_head_index + 1)
        return max_width