'''
Given a reference of a node in a connected 
undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) 
and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from collections import deque
class Solution:
    def cloneGraph(self, start: 'Node') -> 'Node':
        if not start:
            return start
        queue = deque()
        queue.append(start)
        visited = dict()
        visited[start] = Node(start.val)
        while queue:
            node = queue.popleft()
            clone = visited[node]
            for nei in node.neighbors:
                if nei not in visited:
                    nei_clone = Node(nei.val)
                    visited[nei] = nei_clone
                    queue.append(nei)
                clone.neighbors.append(visited[nei])
        return visited[start]