# Minimum Path Sum
# Difficulty: Medium
# Language: c

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
 
    int dp[m][n];
     
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            dp[i][j] = 0;
        }
    } 
    int traversefun(int i, int j) {
        if(i >= m || j >= n) {
            return 2147483647;  
        }
        else if(i == m-1 && j == n-1) {
            dp[i][j] = grid[i][j];
            return dp[i][j];
        }
        else if(dp[i][j] != 0) {
            return dp[i][j];
        }

        int down = traversefun(i+1, j);
        int right = traversefun(i, j+1);

        dp[i][j] = (down < right ? down : right) + grid[i][j];
        return dp[i][j];
    }

    traversefun(0, 0);
    return dp[0][0];
}

