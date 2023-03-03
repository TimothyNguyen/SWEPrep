import collections
def bfs(graph, start):
    queue = collections.deque(start)
    visited = set()
    visited.add(start)
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if node not in visited:
                visited.add(node)
                queue.append(nei)
    

    