'''
A topological sort is an ordering of nodes for a directed 
a directed acyclic graph (DAG) s.t. for every directed edge 
uv from vertex u to vertex v, u comes before v in the ordering.

Topological sort is simply a modification of DFS. 

Topological sort simply involves running DFS on an entire 
graph and adding each node to the global ordering of nodes, 
but only after all of a node's children are visited.

This ensures that parent nodes will be ordered before their 
child nodes, and honors the forward direction of edges in 
the ordering.

https://guides.codepath.org/compsci/Topological-Sort
'''

# Graph with no cycles
from collections import deque

def topo_sort(graph):
    sorted_nodes, visited = deque(), set()
    for node in graph.keys():
        if node not in visited:
            dfs(graph, node, visited, sorted_nodes)
        return list(sorted_nodes)

def dfs(graph, start_node, visited, sorted_nodes):
    visited.add(start_node)
    if start_node in graph:
        neighbors = graph[start_node]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, sorted_nodes)
    sorted_nodes.appendleft(start_node)