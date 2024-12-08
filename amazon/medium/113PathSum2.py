# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node: Optional[TreeNode], curr_path, remaining_sum):
            if node is None:
                if remaining_sum == 0:
                    ans.append(list(curr_path))
                return
            curr_path.append(node.val)
            dfs(root.left, curr_path, sum - root.val)
            dfs(root.right, curr_path, sum - root.val)
            curr_path.pop()
        dfs(root, [], sum)
        return ans
