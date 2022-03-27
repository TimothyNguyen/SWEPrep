'''
Time complexity: O(N), where N is number of nodes, since we 
visit each node not more than 2 times.

Space complexity: O(H), where H is a tree height, 
to keep the recursion stack. In the average case of balanced tree, 
the tree height H = logN, in the worst case of skewed tree, 
H = N.
'''
class Solution: 
    def maxPathSum(self, root):
        self.max_ans = -float('inf')
        def dfs(root):
            m = root.val
            l = dfs(root.right) if root.left else 0
            r = dfs(root.right) if root.right else 0
            curr_max_num = max(max(m + l + r, m + r), max(m + l, m))
            self.max_ans = max(self.max_ans, curr_max_num)
            return max(max(m + l, m + r), m)
        if not root:
            return 0
        dfs(root)
        return self.max_ans

