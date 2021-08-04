class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid[obstacleGrid.length-1][obstacleGrid[0].length-1] == 1) return 0;
        for(int r = 0; r < obstacleGrid.length && obstacleGrid[r][0] != 1; r++) obstacleGrid[r][0] = -1;
        for(int c = 0; c < obstacleGrid[0].length && obstacleGrid[0][c] != 1; c++) obstacleGrid[0][c] = -1;
        for(int r = 1; r < obstacleGrid.length; r++) {
            for(int c = 1; c < obstacleGrid[0].length; c++) {
                if(obstacleGrid[r][c] == 1) continue;
                obstacleGrid[r][c] += ((obstacleGrid[r-1][c] != 1) ? obstacleGrid[r-1][c] : 0) +  ((obstacleGrid[r][c-1] != 1) ? obstacleGrid[r][c-1] : 0);
            }
        }
        return -obstacleGrid[obstacleGrid.length-1][obstacleGrid[0].length-1];
    }
}