# https://leetcode.com/problems/frog-position-after-t-seconds/
'''
Given an undirected tree consisting of n vertices numbered from 1 to n. 
A frog starts jumping from vertex 1. In one second, the frog jumps 
from its current vertex to another unvisited vertex if they are 
directly connected. The frog can not jump back to a visited vertex. 
In case the frog can jump to several vertices, it jumps randomly 
to one of them with the same probability. Otherwise, when the frog 
can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, 
where edges[i] = [ai, bi] means that exists an edge connecting 
the vertices ai and bi.

Return the probability that after t seconds the frog is on 
the vertex target.
'''
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        
        # 1. Construct the graph with adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # create a list to keep track the probabilities
        probabilities = [0 for x in range(n+1)]
        
        # Probability of jumping to 1 at the beginning is 1
        probabilities[1] = 1
        
        current_node = [1]
        for current_time in range(t):
            next_node = []
            for neighbor in current_node:
                # Get a list of unvisited nodes
                neighbors = list()
                for child in graph[neighbor]:
                    if probabilities[child] == 0: 
                        neighbors.append(child)
                
                # Check to see if we found the target
                if neighbor == target:
                    # If there's no place to jump away
                    if len(neighbors) == 0:
                        # return current probability
                        return probabilities[neighbor]
                
                for child in neighbors:
                    # Calculate the probability of each neighbor of neighbors
                    probabilities[child] = probabilities[neighbor] * 1.0 / len(neighbors)
                    # you need to assemble the next node
                    next_node.append(child)
                
            current_node = next_node
                
        return probabilities[target] if target in current_node else 0                
                