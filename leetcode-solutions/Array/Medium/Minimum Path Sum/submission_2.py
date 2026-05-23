# Problem: Minimum Path Sum
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        def traversefun(i,j):
            if i>=m or j>=n:
                return float('inf')
            elif i==m-1 and j==n-1:
                dp[i][j]=grid[i][j]
                return dp[i][j]
            elif dp[i][j]!=0:
                return dp[i][j]
            dp[i][j]=min(traversefun(i+1,j),traversefun(i,j+1))+grid[i][j]
            return dp[i][j]
        startrow,startcol=0,0
        traversefun(startrow,startcol)
        return dp[0][0]
