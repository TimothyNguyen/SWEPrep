'''
A maze consists of n rooms numbered from 1 to n, and some rooms are
connected by corridors. You are given a 2D integer array corridors 
where corridors[i] = [room1i, room2i] indicates that there is a 
corridor connecting room1i and room2i, allowing a person in the 
maze to go from room1i to room2i and vice versa.

The designer of the maze wants to know how confusing the maze is. 
The confusion score of the maze is the number of different cycles 
of length 3.

For example, 1 → 2 → 3 → 1 is a cycle of length 3, but 
1 → 2 → 3 → 4 and 1 → 2 → 3 → 2 → 1 are not.
Two cycles are considered to be different if one or more of the 
rooms visited in the first cycle is not in the second cycle.

Example: 
5
[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]

Output of graph & set:
defaultdict(<class 'list'>, {1: [2, 4, 3], 2: [5, 4], 3: [4]})
{(2, 1), (4, 3), (3, 1), (4, 2), (4, 1), (5, 2)}

Time Complexity:  O(V*E^2)
'''
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    
class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = Graph(n)
        s = set()
        
        for start, end in corridors:
            if start < end:
                graph.add_edge(start, end)
                s.add((end, start))
            else:
                graph.add_edge(end, start)
                s.add((start, end))
        
        ans = 0
        for node in range(1, n + 1):
            for nei in graph.graph[node]:
                for nei_nei in graph.graph[nei]:
                    ans += 1 if (nei_nei, node) in s else 0
        return ans