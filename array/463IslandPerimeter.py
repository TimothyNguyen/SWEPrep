class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # Look north
                    if r == 0 or grid[r - 1][c] == 0:
                        perimeter += 1
                    # Look south
                    if r + 1 == len(grid) or grid[r + 1][c] == 0:
                        perimeter += 1
                    # Look west
                    if c == 0 or grid[r][c - 1] == 0:
                        perimeter += 1
                    # Look east
                    if c + 1 == len(grid[0]) or grid[r][c+1] == 0:
                        perimeter += 1
        return perimeter