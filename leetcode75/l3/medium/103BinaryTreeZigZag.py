'''
Given the root of a binary tree, return the zigzag level order traversal 
of its nodes' values. (i.e., from left to right, then right to left for 
the next level and alternate between).

Time/Space: O(n) 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        if not root: return ans
        queue.append(root)
        l = 0
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if len(level) > 0:
                if l % 2 == 1: level.reverse()
                ans.append(level)
            l += 1
        return ans
            
            