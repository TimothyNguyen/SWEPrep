'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections 
forming a network where connections[i] = [ai, bi] represents a connection between computers 
ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between 
two directly connected computers, and place them between any pair of disconnected computers 
to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers 
connected. If it is not possible, return -1.

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = defaultdict(list)
        visited = [0 for _ in range(n)]
        
        def dfs(i):
            visited[i] = 1
            for nei in graph[i]:
                if visited[nei] == 0:
                    dfs(nei)
        
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count - 1