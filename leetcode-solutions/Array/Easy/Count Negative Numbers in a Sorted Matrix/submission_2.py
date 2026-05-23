# Problem: Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in grid[i][::-1]:
                if grid[i][0]<0:
                    count+=n
                    break
                elif grid[i][n-1]>0:
                    break
                else:
                    if j>=0:
                        break
                    else:
                        count=count+1
        return count


