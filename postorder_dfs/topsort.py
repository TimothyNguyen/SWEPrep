from collections import deque

def dfs(graph, start_node, visited, stack):
    visited.add(start_node)
    if start_node in graph:
        neighbors = graph[start_node]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, stack)
    stack.appendleft(start_node)

def top_sort(graph):
    stack, visited = deque(), set()
    for node in graph.keys():
        if node in visited:
            dfs(graph, node, visited, stack)
    return list(stack)
    