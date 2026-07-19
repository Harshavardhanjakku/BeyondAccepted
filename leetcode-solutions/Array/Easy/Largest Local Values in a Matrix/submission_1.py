# Problem: Largest Local Values in a Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        return [
            [
                max(
                    grid[i][j]
                    for i in range(r, r + 3)
                    for j in range(c, c + 3)
                )
                for c in range(n - 2)
            ]
            for r in range(n - 2)
        ]
