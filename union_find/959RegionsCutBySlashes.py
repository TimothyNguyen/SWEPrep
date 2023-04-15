'''
One "brute force" way to specify the graph is to associate each grid square with 4 nodes (north, south, west, and east), representing 4 triangles inside the square if it were to have both slashes. 

Then, we can connect all 4 nodes if the grid square is " ", and connect two pairs if the grid square is "/" or "\". 

Finally, we can connect all neighboring nodes (for example, the east node of the square at grid[0][0] connects with the west node of the square at grid[0][1]).
'''
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        self.parent[pi] = pj

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 1
        n = len(grid)
        uf = UF(4 * n * n)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * n + c)
                if val in '/ ':
                    uf.union(root + 0, root + 1)
                    uf.union(root + 2, root + 3)
                if val in '\ ':
                    uf.union(root + 0, root + 2)
                    uf.union(root + 1, root + 3)
            
                # north/south
                if r + 1 < n:
                    uf.union(root + 3, (root + 4 * n) + 0)
                if r - 1 >= 0:
                    uf.union(root + 0, (root - 4 * n) + 3)
                # east/west
                if c + 1 < n:
                    uf.union(root + 2, (root + 4) + 1)
                if c - 1 >= 0:
                    uf.union(root + 1, (root - 4) + 2)
        ans = 0
        for x in range(4 * n * n):
            parent_x = uf.find(x)
            if parent_x == x:
                ans += 1
        return ans
