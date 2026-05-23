# Problem: Number of Islands
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 
            else:
                if grid[i][j]=="1":
                    grid[i][j]="2" 
                    dfs(grid,i,j-1)
                    dfs(grid,i,j+1)
                    dfs(grid,i+1,j)
                    dfs(grid,i-1,j)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    count+=1
        return count
        


        
