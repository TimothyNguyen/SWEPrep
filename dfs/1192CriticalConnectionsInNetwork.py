'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server 
connections forming a network where connections[i] = [ai, bi] represents a connection 
between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to 
reach some other server.

Return all critical connections in the network in any order.

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

https://leetcode.com/problems/critical-connections-in-a-network/solution/

Time Complexity: O(V + E)O(V+E) where V represents the number of vertices and E 
represents the number of edges in the graph. We process each node exactly once thanks
to the rank dictionary also acting as a "visited" safeguard at the top of the dfs function. 
Since the problem statement mentions that the graph is connected, that means E >= V
 and hence, the overall time complexity would be dominated by the number of edges i.e. O(E).

Space Complexity: O(E)O(E). The overall space complexity is a sum of the space occupied 
by the connDict dictionary, rank dictionary, and graph data structure. E + V + (V + E)E+V+(V+E) = O(E)O(E).
'''
class Solution:
    
    rank = {}
    graph = defaultdict(list)
    conn_dict = {}
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.formGraph(n, connections)
        self.dfs(0, 0)
        
        result = []
        for u, v in self.conn_dict:
            result.append([u, v])
        
        return result
            
    def dfs(self, node: int, discovery_rank: int) -> int:
        
        # That means this node is already visited. We simply return the rank.
        if self.rank[node]:
            return self.rank[node]
        
        # Update the rank of this node.
        self.rank[node] = discovery_rank
        
        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            
            # Skip the parent.
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue
                
            # Recurse on the neighbor.    
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            
            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]
            
            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)
        
        return min_rank
    
    def formGraph(self, n: int, connections: List[List[int]]):
        
        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}
        
        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None
        
        for edge in connections:
            
            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            
            self.conn_dict[(min(u, v), max(u, v))] = 1