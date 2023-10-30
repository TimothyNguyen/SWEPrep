"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque([root])
        num_elements = len(queue)
        prev_node = None
        while queue:
            node = queue.popleft()
            if prev_node:
                prev_node.next = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            num_elements -= 1
            if num_elements == 0:
                # print(node.val)
                num_elements = len(queue)
                # print(num_elements)
                prev_node = None
                node.next = None
            else:
                prev_node = node
        return root
