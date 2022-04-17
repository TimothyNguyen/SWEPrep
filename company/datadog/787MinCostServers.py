from collections import defaultdict
import heapq

def min_time(server_graph: List[List[int]], start, end):
    graph = defaultdict(list)
    unique_nodes = defaultdict(int)
    num_elements = 0
    for start, end, cost in server_graph:
        if start not in unique_nodes:
            unique_nodes[start] = num_elements
            num_elements += 1
        if end not in unique_nodes:
            unique_nodes[end] = num_elements
            num_elements += 1
        server_graph[start].append((end, cost))
    dist = [float('inf')] * num_elements
    dist[start] = 0
    heap = [(0, start)]
    parent = dict()
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            break
        for nei, c in graph[node]:
            if cost + c < dist[unique_nodes[node]]:
                parent[nei] = node
                dist[unique_nodes[node]] = c
                heapq.heappush(heap, (cost + c, nei))
    
    ans = []
    if dist[end] < float('inf'):
        ans.append(node)
        while node in parent:
            ans.append(parent[node])
            node = parent[node]
    ans.reverse()
    return dist[end], ans
        