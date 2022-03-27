'''
You are given a network of n nodes, labeled from 
1 to n. You are also given times, a list of travel 
times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, 
and wi is the time it takes for a signal to travel 
from source to target.

We will send a signal from a given node k. Return 
the time it takes for all the n nodes to receive the 
signal. If it is impossible for all the n nodes to 
receive the signal, return -1. 

times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

Time: O(N*E)
Space: O(N*E)
'''
import collections
import heapq
from this import d
class Solution:
    '''
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        
        heap = [(0, k)] # (time, node), init heap with 0 time and node k
        timeMap = dict() # For record node and time
        while heap:
            time, node = heapq.heappop(heap)
            if node not in timeMap: # avoid visiting the same node
                timeMap[node] = time
                for nextNode, nextTime in graph[node]:
                    heapq.heappush(heap, (time + nextTime, nextNode))
        
        if len(timeMap)== n:
            return max(timeMap.values())
        return -1 
    '''

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for i, j, w in times:
            graph[i][j] = w
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        visited = dict()
        while heap:
            time, node = heapq.heappop(heap)
            if node not in visited:
                visited[node] = time
                for child in graph[node]:
                    if graph[node][child] + d < dist[child]:
                        dist[child] = graph[node][child] + d
                        heapq.heappush(heap, (dist[child], child))
        ret =  max(dist[1:])
        return ret if ret!=float("inf") else -1
