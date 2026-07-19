# Problem: Find a Safe Walk Through a Grid
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def findSafeWalk(self, grid, health):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1] * cols for _ in range(rows)]
        def dfs(i, j, health):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            health -= grid[i][j]
            if health <= 0:
                return False
            if health <= dp[i][j]:
                return False
            dp[i][j] = health
            if i == rows - 1 and j == cols - 1:
                return True
            return (
                dfs(i - 1, j, health) or
                dfs(i + 1, j, health) or
                dfs(i, j - 1, health) or
                dfs(i, j + 1, health)
            )
        return dfs(0, 0, health)
