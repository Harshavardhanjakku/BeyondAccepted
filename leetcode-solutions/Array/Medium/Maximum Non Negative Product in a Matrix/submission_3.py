# Problem: Maximum Non Negative Product in a Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def maxProductPath(self, grid):
        nor=len(grid)
        noc=len(grid[0])
        maxdp=[[0]*noc for _ in range(nor)]
        mindp=[[0]*noc for _ in range(nor)]
        maxdp[0][0]=grid[0][0]
        mindp[0][0]=grid[0][0]
        for c in range(1,noc):
            maxdp[0][c]=maxdp[0][c-1]*grid[0][c]
            mindp[0][c]=mindp[0][c-1]*grid[0][c]
        for r in range(1,nor):
            maxdp[r][0]=maxdp[r-1][0]*grid[r][0]
            mindp[r][0]=mindp[r-1][0]*grid[r][0]
        for r in range(1,nor):
            for c in range(1,noc):
                val=grid[r][c]
                a=maxdp[r-1][c]*val
                b=mindp[r-1][c]*val
                d=maxdp[r][c-1]*val
                e=mindp[r][c-1]*val
                maxdp[r][c]=max(a,b,d,e)
                mindp[r][c]=min(a,b,d,e)
        res=maxdp[nor-1][noc-1]
        return res%(10**9+7) if res>=0 else -1
