'''
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi 
with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst 
with at most k stops. If there is no such route, return -1.

Time Complexity: Let E represent the number of flights and V represent the number of cities. The 
time complexity is mainly governed by the number of times we pop and push into the heap. We will 
process each node (city) atleast once and for each city popped from the queue, we iterate over its 
adjacency matrix and can potentially add all its neighbors to the heap. Thus, the time taken for 
extract min and then addition to the heap (or simply, heap replace) would be O(V^2⋅log V).

Space: O(V^2)
V is occupied by the two dictionaries and also by the heap and V^2 by the adjacency matrix structure.
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
        
        dist = [(float('inf'), float('inf')) for _ in range(n)]
        
        dist[src] = (0, 0)
        heap = [(0, 0, src)]
        parent = dict()
        while heap:
            cost, hops, node = heapq.heappop(heap)
            
            if node == dst and hops <= k + 1:
                return cost
            if hops == k + 1:
                continue
            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, dist[nei][0], adj_matrix[node][nei]
                    # Better cost?
                    if dU + wUV < dV:
                        dist[nei] = ((dU + wUV, hops))
                        heapq.heappush(heap, (dU + wUV, hops + 1, nei))
                        # current_stops[nei] = stops
                    elif hops < dist[nei][1]:
                        #  Better steps?
                        heapq.heappush(heap, (dU + wUV, hops + 1, nei))
        '''
        ans = []
        node = dst
        if dist[dst][0] < float('inf'):
            ans.append(node)
            while node in parent:
                ans.append(parent[node])
                node = parent[node]
        ans.reverse()
        '''
        return -1 if dist[dst][0] == float("inf") else dist[dst][0]