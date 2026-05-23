# Path with Maximum Gold
# Difficulty: Medium
# Language: python

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        def traversal(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 0
            elif visited[i][j]:
                return 0
            visited[i][j]=True
            left=traversal(i,j-1)
            right=traversal(i,j+1)
            top=traversal(i-1,j)
            down=traversal(i+1,j)
            result=max(left,right,top,down)+grid[i][j]
            visited[i][j]=False
            return result
        maxi=float('-inf')
        for row in range(m):
            for col in range(n):
                res=traversal(row,col)
                maxi=max(maxi,res)
        return  maxi
