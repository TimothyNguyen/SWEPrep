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

        queue = [start]
        visited = dict()
        visited[start] = Node(start.val)
        while queue:
            node = queue.pop(0)
            clone = visited[node]
            for nei in node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)
                clone.neighbors.append(visited[nei])
        return visited[start]