'''
There are n cities connected by some number of flights. You are given an array 
flights where flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from 
src to dst with at most k stops. If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],
                         [1,2,100],
                         [2,0,100],
                         [1,3,600],
                         [2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

2. You are working with the microservices architecture and you have a graph of servers.
Each server is represented with its IP address. You know the duration of sending your data
from server[i] to server[j]. As an input, you have an IP address from the starting server and the end
server and you need to find the path from the 'start' to 'end' which takes the minimum amount of time
and show its path.
'''
import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, target, cost in flights:
            graph[start].append((target, cost))
        
        dist = [(float('inf'), float('inf')) for _ in range(n)]
        dist[src] = (0, 0)
        heap = [(0, 0, src)]
        parent = dict()
        final_cost = -1
        while heap:
            cost, hops, node = heapq.heappop(heap)
            if node == dst and hops <= k + 1:
                final_cost = cost
                break
            if hops == k + 1:
                continue
            for nei, nei_cost in graph[node]:
                if cost + nei_cost >= dist[nei][0] and hops + 1 >= dist[nei][1]:
                    continue
                dist[nei] = ((cost + nei_cost, hops + 1))
                heapq.heappush(heap, (cost + nei_cost, hops + 1, nei))
                parent[nei] = node
        '''
        ans = []
        node = dst
        if dist[dst][0] < float('inf'):
            ans.append(node)
            while node in parent:
                ans.append(parent[node])
                node = parent[node]
        ans.reverse()
        # print(ans)
        '''
        return final_cost
class Solution:
    # O(n) --> all nodes
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K:int) -> int:
        # Build graph
        graph = collections.defaultdict(list)
        for s, e, c in flights:
            graph[s].append((e, c))
        
        dist = [(float('inf'), float('inf'))] * n
        q = collections.deque([(src, 0)]) # (node, cost)
        stops = -1
        while len(q) > 0 and stops < K:
            stops += 1
            same_level_counts = len(q)
            for i in range(same_level_counts):
                node, costs = q.popleft()
                for nextNode, nextCost in graph[node]:
                    if costs + nextCost < dist[nextNode]:
                        dist[nextNode] = costs + nextCost
                        q.append((nextNode, costs + nextCost))
        return - 1 if dist[dst] == float('inf') else dist[dst]
