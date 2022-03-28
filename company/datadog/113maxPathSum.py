class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def max_Path_sum(self, root):
        ans = []
        max_sum = -float('inf')
        def dfs(curr_sum, root, path):
            path.append(root.val)
            if root.left == None and root.right == None:
                if curr_sum + root.val > max_sum:
                    max_sum = curr_sum + root.val
                    ans = path
                return
            if root.left:
                dfs(root.val + curr_sum, root.left, path) 
            if root.right:
                dfs(root.val + curr_sum, root.right, path)
        if root:
            dfs(0, root, [])
        return ans