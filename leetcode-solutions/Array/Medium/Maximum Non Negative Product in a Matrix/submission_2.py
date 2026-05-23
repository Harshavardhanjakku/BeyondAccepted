# Problem: Maximum Non Negative Product in a Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maxProductPath(self, grid):
        MOD=10**9+7
        m=len(grid)
        n=len(grid[0])
        memo={}
        def dfs(i,j):
            if i>=m or j>=n:
                return (float('-inf'),float('inf'))
            if (i,j) in memo:
                return memo[(i,j)]
            if i==m-1 and j==n-1:
                return (grid[i][j],grid[i][j])
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            mx=max(down[0],right[0])
            mn=min(down[1],right[1])
            val=grid[i][j]
            if val<0:
                mx,mn=mn,mx
            mx*=val
            mn*=val
            memo[(i,j)]=(mx,mn)
            return memo[(i,j)]
        res=dfs(0,0)[0]
        if res<0:
            return -1
        return res%MOD
