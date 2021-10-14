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
        if not start:
            return start
        queue = [start]
        visited = dict()
        visited[start] = Node(start.val)
        while queue:
            node = queue.pop(0)
            clone_node = visited[node]
            for nei in node.neighbors:
                if nei not in visited:
                    new_node = Node(nei.val)
                    visited[nei] = new_node
                    queue.append(nei)
                clone_node.neighbors.append(visited[nei])
        return visited[start]