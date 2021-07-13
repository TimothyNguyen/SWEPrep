from collections import defaultdict

class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = defaultdict(set)
        self.indegs = [0] * n
    
    def addEdges(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)
        self.indegs[u] += 1
        self.indegs[v] += 1
    
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        g = Graph(n)

        for start, end in roads:
            g.addEdges(start, end)
        
        maxCount = -1
        for i in range(n):
            for j in range(i + 1, n):
                common = -1 if i in g.graph[j] or j in g.graph[i] else 0
                curr = g.indegs[i] + g.indegs[j] - common
                maxCount = max(curr, maxCount)
        return maxCount