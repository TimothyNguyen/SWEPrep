"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, start: Optional['Node']) -> Optional['Node']:
        if not start:
            return start
        queue = deque([start])
        visited = dict()
        visited[start] = Node(start.val)
        while queue:
            node = queue.popleft()
            clone = visited[node]
            for nei in node.neighbors:
                if nei not in visited:
                    new_nei_clone = Node(nei.val)
                    visited[nei] = new_nei_clone
                    queue.append(nei)
                clone.neighbors.append(visited[nei])
        return visited[start]
