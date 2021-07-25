# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans = ""
        visited, stack = set(), [root]
        while stack:
            temp = stack[-1]
            if temp in visited:
                stack.pop()
                ans += ")"
            else:
                visited.add(temp)
                ans += "(" + str(temp.val)
                if not temp.left and temp.right: ans += "()"
                if temp.right: stack.append(temp.right)
                if temp.left: stack.append(temp.left)
        return ans[1:len(ans)-1]
                