# Problem: Longest Increasing Path in a Matrix
# Difficulty: Hard
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0 for i in range(cols)] for j in range(rows)]
        
        def dfs(r,c,prev):
            if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c] <= prev:
                return 0
            if dp[r][c]:
                return dp[r][c]
            
            res=1
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))            
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))    
            
            dp[r][c]=res
            return res
                   
        res=0
        for r in range(rows):
            for c in range(cols):
                res=max(res,dfs(r,c,-1))
        return res

