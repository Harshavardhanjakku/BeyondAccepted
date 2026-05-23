# Problem: Maximum Non Negative Product in a Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maxProductPath(self, grid):
        MOD=10**9+7
        nor=len(grid)
        noc=len(grid[0])
        dp=[[None]*noc for _ in range(nor)]
        def dfs(r,c):
            if r>=nor or c>=noc:
                return (float('-inf'),float('inf'))
            if dp[r][c]:
                return dp[r][c]
            if r==nor-1 and c==noc-1:
                return (grid[r][c],grid[r][c])
            right=dfs(r,c+1)
            down=dfs(r+1,c)
            mx=max(right[0],down[0])
            mn=min(right[1],down[1])
            val=grid[r][c]
            if val<0:
                mx,mn=mn,mx
            mx*=val
            mn*=val
            dp[r][c]=(mx,mn)
            return dp[r][c]
        res=dfs(0,0)[0]
        return res%MOD if res>=0 else -1
