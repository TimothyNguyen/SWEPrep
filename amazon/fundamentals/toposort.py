'''
Utilizes DFS

Visits each node in the graph and ensures that all 
its dependencies are visited before adding to topological order

Good to check for prerequistes or ordering
'''

from collections import defaultdict
def topo_sort_dfs(graph, node, visited, stack):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            topo_sort_dfs(graph, nei, visited, stack)
    stack.append(node)

def topo_sort(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            topo_sort_dfs(graph, node, visited, stack)
    return stack[::-1]

graph = defaultdict(list)
graph['A'].extend(['B', 'C'])
graph['B'].extend(['D'])
graph['C'].extend(['D'])
graph['D'].extend(['E'])
graph['F'].extend(['C'])
topo_order = topo_sort(graph)