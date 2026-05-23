# Unique Paths II
# Difficulty: Medium
# Language: python

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        dp=[[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(i,j):
            if i>=rows or  j>=cols or obstacleGrid[i][j]==1:
                return 0
            elif i==rows-1 and j==cols-1:
                dp[i][j]=1
                return dp[i][j] 
            elif dp[i][j]:
                return dp[i][j]
            dp[i][j]=dfs(i+1,j)+dfs(i,j+1)        
            return dp[i][j]
        startrow,startcol=0,0
        dfs(startrow,startcol)
        return dp[0][0]
