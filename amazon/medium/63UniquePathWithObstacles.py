class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for r in range(len(obstacleGrid)):
            if obstacleGrid[r][0] == 1:
                break
            obstacleGrid[r][0] = -1
        for c in range(len(obstacleGrid[0])):
            if obstacleGrid[0][c] == 1:
                break
            obstacleGrid[0][c] = -1
        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                if obstacleGrid[r][c] != 1:
                    obstacleGrid[r][c] = min(obstacleGrid[r-1][c], 0) + min(obstacleGrid[r][c-1], 0)
        return -min(obstacleGrid[-1][-1], 0)