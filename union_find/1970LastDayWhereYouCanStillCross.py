'''
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are 
given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes 
flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] 
represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) 
will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only 
walking on land cells. You can start from any cell in the top row and end at any cell in the
bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only
walking on land cells.


Naive approach: Find the possible path from the top row to the bottom row for every cell
    - Pretty slow: O(4 * n * m^2)
    - n * m = size of the cells
    - m = number of columns
    - 4 * represent the number of columns

How to use union find

UnionFind:
    find(): Used to find the parent of the cell to which the cell is connected
    union(): This will connect two cells in the grid
    find_index(): Identify the index in the grid and maps it into a 1-D array

- You need to check if the first & last indexes are the same

1. Make connections between cells.
2. Connect the current cell to the first index in 1-D array if it belongs to the 
top row. Otherwise connect to the last index if the cell belongs to the bottom row.
3. Find the respective parent.
4. Verify the connection from the top to the bottom.
5. Repeat the process until all the cells are traversed.
'''

class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] = self.size[root_x]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[1] * col for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 0
            index_1 = r * col + c + 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                index_2 = new_r * col + new_c + 1
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 0:
                    dsu.union(index_1, index_2)
                    
            if r == 0:
                dsu.union(0, index_1)
            if r == row - 1:
                dsu.union(row * col + 1, index_1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i