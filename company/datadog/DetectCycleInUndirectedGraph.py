# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
'''
Time Complexity: O(V+E). 
The program does a simple DFS Traversal of the graph which is represented 
using adjacency list. So the time complexity is O(V+E).
Space Complexity: O(V). 
To store the visited array O(V) space is required.

'''
from collections import defaultdict

class Graph:
    def __init(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def isCyclic(self):

        def dfs(v, parent):
            visited[v] = True

            for i in range(self.v):
                if not visited[i]:
                    if dfs(i, v):
                        return True
                # If an adjacent vertex is
                # visited and not parent
                # of current vertex,
                # then there is a cycle
                elif visited[i] and parent != i:
                    return True
            return False

        visited = [False] * self.v
        for i in range(self.v):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False