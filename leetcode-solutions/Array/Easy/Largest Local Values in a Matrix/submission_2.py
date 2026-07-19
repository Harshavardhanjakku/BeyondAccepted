# Problem: Largest Local Values in a Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        row_max = [[0] * (n - 2) for _ in range(n)]

        for r in range(n):
            for c in range(n - 2):
                row_max[r][c] = max(grid[r][c], grid[r][c + 1], grid[r][c + 2])

        res = [[0] * (n - 2) for _ in range(n - 2)]

        for r in range(n - 2):
            for c in range(n - 2):
                res[r][c] = max(row_max[r][c], row_max[r + 1][c], row_max[r + 2][c])

        return res
