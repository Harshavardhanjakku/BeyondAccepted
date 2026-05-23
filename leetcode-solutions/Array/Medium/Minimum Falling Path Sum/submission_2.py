# Problem: Minimum Falling Path Sum
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[float('inf')]*n for _ in range(n)]
        def myfun(row,col):
            if col<0 or row<0 or col>=n or row>=n:
                return float('inf')
            if row==n-1:
                return matrix[row][col]
            if dp[row][col]!=float('inf'):
                return dp[row][col]
            dp[row][col]=matrix[row][col]+min(myfun(row + 1, col - 1), myfun(row + 1, col),  myfun(row + 1, col + 1))
            return dp[row][col]
        for c in range(n):
            dp[0][c]=myfun(0,c)
        return min(dp[0])

