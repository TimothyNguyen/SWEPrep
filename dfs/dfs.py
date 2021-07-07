def depth_first_search(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # If a node with no outgoing edges won't be
            # included in the adjacency list, we need to check
            if vertex in graph:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    return visited