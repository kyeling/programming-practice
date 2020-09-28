class Solution {
    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int h = grid.length;
        int w = grid[0].length;
        int count = 0;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                if(grid[i][j] == '1'){
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
    public void dfs(char[][]grid, int i, int j){
        int h = grid.length;
        int w = grid[0].length;
        if(i < 0 || i >= h || j < 0 || j >= w || grid[i][j] == '0'){
            return;
        }
        grid[i][j] = '0';
        dfs(grid, i+1, j);
        dfs(grid, i, j+1);
        dfs(grid, i-1, j);
        dfs(grid, i, j-1);
    }
}

/* 

block visiting by setting back to 0
base case: when reach water (0) or out of bounds, stop
root node triggers dfs

*/
