'''
There are n cities. Some of them are connected, while some are 
not. If city a is connected directly with city b, and city b 
is connected directly with city c, then city a is connected
indirectly with city c.

A province is a group of directly or indirectly connected 
cities and no other cities outside of the group.

You are given an n x n matrix isConnected where 
isConnected[i][j] = 1 if the ith city and the jth city are 
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        ans = 0
        
        def dfs(visited, isConnected, city):
            for index, neighbor in enumerate(isConnected[city]):
                if index not in visited and neighbor == 1:
                    visited.add(index)
                    dfs(visited, isConnected, index)
        
        for city in range(len(isConnected)):
            if city not in visited:
                ans += 1
                visited.add(city)
                dfs(visited, isConnected, city)
        return ans
# O(n^2) time, O(n) space