# Problem: Construct Product Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def constructProductMatrix(self, grid):
        MOD=12345
        m=len(grid)
        n=len(grid[0])
        p=[[1]*n for _ in range(m)]
        pro=1
        zflag=False
        zc=0
        zpro=1
        for i in grid:
            for j in i:
                if j==0:
                    zflag=True
                    zc+=1
        if zc>1:
            return [[0]*n for _ in range(m)]
        if zc==1:
            for i in range(m):
                for j in range(n):
                    if grid[i][j]!=0:
                        zpro=(zpro*grid[i][j])%MOD
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==0:
                        p[i][j]=zpro%MOD
                    else:
                        p[i][j]=0
            return p
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    p[i][j]=1
                elif j==0:
                    p[i][j]=(p[i-1][n-1]*grid[i-1][n-1])%MOD
                else:
                    p[i][j]=(p[i][j-1]*grid[i][j-1])%MOD
        pro=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                p[i][j]=(p[i][j]*pro)%MOD
                pro=(pro*grid[i][j])%MOD
        return p
