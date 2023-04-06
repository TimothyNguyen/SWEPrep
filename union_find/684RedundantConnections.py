class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent, rank = [], [1] * (n + 1)
        for i in range(n + 1):
            parent.append(i)
        ans = []
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]
                   
        def union(v1, v2):
            p1, p2 = find_parent(v1), find_parent(v2)
            if p1 == p2:
                return False
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
            
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
        return ans
