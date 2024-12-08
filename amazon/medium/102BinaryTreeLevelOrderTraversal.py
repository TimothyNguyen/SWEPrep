# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        ans = []
        size_of_level = 1
        while queue:
            curr_size = 0
            curr_level_res = []
            for i in range(size_of_level):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                    curr_size += 1
                if curr_node.right:
                    queue.append(curr_node.right)
                    curr_size += 1
                curr_level_res.append(curr_node.val)
            ans.append(curr_level_res)
            size_of_level = curr_size
        return ans