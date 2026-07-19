# Problem: Largest Local Values in a Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        res=[[0]*(n-2) for _ in range(n-2)]
        def checkmaxi(i,j,k,l):
            maxi=0
            for row in range(i,k):
                for col in range(j,l):
                    maxi=max(maxi,grid[row][col])
            return maxi
        for r in range(n-2):
            for c in range(n-2):
                res[r][c]=checkmaxi(r,c,r+3,c+3)
        return res
                
