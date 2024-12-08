class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.n = n
        self.size = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)
        if p1 != p2:
            self.size -= 1
            self.parent[p2] = p1

    def get_size(self):
        return self.size

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        idx = 0
        d = {}
        if not grid:
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    d[r, c] = idx
                    idx += 1
        uf = UnionFind(idx)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    if r > 0 and grid[r-1][c] == '1':
                        uf.union(d[r-1,c], d[r,c])
                    if c > 0 and grid[r][c-1] == '1':
                        uf.union(d[r,c-1], d[r,c])
        # print(uf.parent)
        return uf.get_size()



