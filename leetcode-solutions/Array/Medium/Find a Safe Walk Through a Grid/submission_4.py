# Problem: Find a Safe Walk Through a Grid
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def findSafeWalk(self, grid, health):
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[-1] * (health + 1) for _ in range(cols)] for _ in range(rows)]
        visited = set()

        def dfs(i, j, health):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False

            health -= grid[i][j]

            if health <= 0:
                return False

            if i == rows - 1 and j == cols - 1:
                return True

            if (i, j, health) in visited:
                return False

            if dp[i][j][health] != -1:
                return dp[i][j][health]

            visited.add((i, j, health))

            dp[i][j][health] = (
                dfs(i - 1, j, health) or
                dfs(i + 1, j, health) or
                dfs(i, j - 1, health) or
                dfs(i, j + 1, health)
            )

            visited.remove((i, j, health))

            return dp[i][j][health]

        return dfs(0, 0, health)
