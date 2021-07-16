# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, start):
        """
        :type node: Node
        :rtype: Node
        """
        if not start: return start
        
        queue = deque([start])
        visited = dict()
        visited[start] = Node(start.val)
        while queue:
            node = queue.popleft()
            clone = visited[node]
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(visited[neighbor])
        return visited[start]