'''
You are given an array points representing integer 
coordinates of some points on a 2D-plane, where 
points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] 
is the manhattan distance between them: 
|xi - xj| + |yi - yj|, where |val| denotes the absolute 
value of val.

Return the minimum cost to make all points connected. 
All points are connected if there is exactly one 
simple path between any two points.

Prim's algorithm 
- A greedy algorithm for building a min spanning tree in a weighted and undirected graph.
In this algorithm, we include an arbitrary node in the MST and keep on adding the 
lowest-weighted edges of the nodes present in the MST until all nodes are included in 
the MST and no cycles are formed.

Algorithm

    1. Initialize some variables:
        n - Number of nodes of the graph.
        mstCost - Cost to build the MST.
        edgesUsed - Number of edges included in the MST.
        inMST - Array to track if a node was already included in
                MST or not.
        heap - A min-heap to pick minimum weight edge, each 
        element of heap is a pair of (edge weight, node).

    2. Initially, we start with node 0 and the cost to include 
    this node will be 0, thus we push all adjacent edges of node 0
    in heap with their respective weights using a for-loop. 
    However, to make the code implementation cleaner, we will 
    simply initialize the heapheapheap with the pair (0, 0), 
    which represents a temporary edge to node 0 with a weight of 0.

    3. We pop elements from the heap and attempt to add them to the tree until edgesUsed 
    becomes equal to n. We initially added one temporary edge, thus we stop when n
    edges are added in the MST.
        - We get the minimum weighted edge and the node from the top of heap and pop it.
        - If this node is already present in our MST (inMST[node]==true) we discard this edge.
        - Otherwise, we include this node in our MST, increment edgesUsed 
        by 1, add the edge's weight to the mstCost, and push the edges of this node 
        into the heap.

    4. We return the total cost of MST, mstCost.

    Prim's Algorithm
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # min heap to store min-edge
        heap = [(0, 0)]
        
        # track nodes
        visited = [False] * n
        
        mst_cost = 0
        edges_used = 0
        
        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)
            
            # if node in MST, discard edge
            if visited[curr_node]:
                continue
            
            visited[curr_node] = True
            mst_cost += weight
            edges_used += 1
            
            for next_node in range(n):
                # If next node not in MST, then edge from curr node to next node
                # can be pushed in pq
                if not visited[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                    heapq.heappush(heap, (next_weight, next_node))
        return mst_cost