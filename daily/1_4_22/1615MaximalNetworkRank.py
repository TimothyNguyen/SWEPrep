'''
There is an infrastructure of n cities with some number of roads connecting these cities. 
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly 
connected roads to either city. If a road is directly connected to both cities, it is 
only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs 
of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire 
infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 
4 roads that are connected to either 0 or 1. The road between 0 
and 1 is only counted once.
'''
from collections import defaultdict

class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = defaultdict(set)
        self.indegrees = [0] * n
    
    def add_edge(self, start, end):
        self.graph[start].add(end)
        self.graph[end].add(start)

        self.indegrees[start] += 1
        self.indegrees[end] += 1

class Solution(object):
    def maximalNetworkRank(self, n: int, roads: List[int]):
        graph = Graph(n)
        for start, end in roads:
            graph.add_edge(start, end)
        
        max_count = -1
        for i in range(n):
            for j in range(i + 1, n):
                common = -1 if i in graph.graph[j] or j in graph.graph[i] else 0
                cur = graph.indegrees[i] + graph.indegrees[j] + common
                max_count = max(cur, max_count)
        return max_count