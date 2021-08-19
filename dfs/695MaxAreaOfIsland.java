class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        if(grid.length == 0 || grid[0].length == 0) return 0;
        int row = grid.length, col = grid[0].length;
        int[] count = new int[1];
        int max = 0;
        for(int r = 0; r < row; r++) {
            for(int c = 0; c < col; c++) {
                if(grid[r][c] == 1) {
                    count[0] = 0;
                    dfs(grid, r, c, count);
                    max = Math.max(max, count[0]);
                }
            }
        }
        return max;
    }
    
    public void dfs(int[][] grid, int r, int c, int[] count) {
        if(r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != 1) return;
        grid[r][c] = -1; // Mark visited
        count[0]++;
        dfs(grid, r - 1, c, count);
        dfs(grid, r + 1, c, count);
        dfs(grid, r, c - 1, count);
        dfs(grid, r, c + 1, count);
    }
}