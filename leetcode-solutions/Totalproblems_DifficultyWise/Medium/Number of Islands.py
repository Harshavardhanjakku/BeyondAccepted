# Number of Islands
# Difficulty: Medium
# Language: python

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!="1":
                return
            if grid[i][j]=="1":
                grid[i][j]="2"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    count+=1
                    dfs(row,col)
        return count


