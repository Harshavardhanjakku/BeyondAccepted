# Problem: Find a Safe Walk Through a Grid
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

from collections import deque
class Solution(object):
    def findSafeWalk(self, grid, health):
        rows=len(grid)
        cols=len(grid[0])
        health-=grid[0][0]
        if health<=0:
            return False
        q=deque()
        q.append((0,0,health))
        visited=set()
        visited.add((0,0))
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            i,j,health=q.popleft()
            if i==rows-1 and j==cols-1:
                return health>=1
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<rows and 0<=nj<cols and (ni,nj) not in visited:
                    new_health=health-grid[ni][nj]
                    if new_health>=1:
                        visited.add((ni,nj))
                        if grid[ni][nj]==0:
                            q.appendleft((ni,nj,new_health))
                        else:
                            q.append((ni,nj,new_health))

        return False
