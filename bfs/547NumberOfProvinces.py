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