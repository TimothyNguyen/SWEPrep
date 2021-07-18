class Solution(object):        
    def eventualSafeNodes(self, g):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        unvisited, visited, satisfied = 0, 1, 2
        graph = defaultdict(int)
        def dfs(node):
            if graph[node] != unvisited: return graph[node] == satisfied
            graph[node] = visited
            for nei in g[node]:
                if graph[nei] == visited or not dfs(nei): return False
            graph[node] = satisfied
            return True
        ans = []
        for i in range(len(g)):
            if dfs(i):
                ans.append(i)
        return ans