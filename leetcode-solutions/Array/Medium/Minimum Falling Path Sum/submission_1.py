# Problem: Minimum Falling Path Sum
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[-1].copy()

        for row in range(len(matrix) - 2, -1, -1):
            new_dp = [None] * len(matrix[0])
            for col in range(len(matrix[0])):
                min_path = dp[col]
                
                if col > 0 and dp[col-1] < min_path:
                    min_path = dp[col-1]
                if col < len(matrix[0]) - 1 and dp[col+1] < min_path:
                    min_path = dp[col+1]

                new_dp[col] = matrix[row][col] + min_path
            dp = new_dp

        return min(dp)
