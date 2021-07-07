from collections import deque
def bfs(graph, start):
    visited, queue = set(), deque(start)
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited