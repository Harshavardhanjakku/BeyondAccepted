# Problem: Find a Safe Walk Through a Grid
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        rows = len(grid)
        cols = len(grid[0])

        health -= grid[0][0]
        if health <= 0:
            return False

        q = deque([(0, 0, health)])

        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = health

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i, j, health = q.popleft()

            if i == rows - 1 and j == cols - 1:
                return True

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < rows and 0 <= nj < cols:
                    new_health = health - grid[ni][nj]

                    if new_health <= 0:
                        continue

                    if new_health <= best[ni][nj]:
                        continue

                    best[ni][nj] = new_health
                    q.append((ni, nj, new_health))

        return False
