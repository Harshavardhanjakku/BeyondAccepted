# Problem: Rotating the Box
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def rotateTheBox(self, boxgrid):
        rows=len(boxgrid)
        cols=len(boxgrid[0])
        for row in range(rows):
            empty=cols-1
            for col in range(cols-1,-1,-1):
                if boxgrid[row][col]=="*":
                    empty=col-1
                elif boxgrid[row][col]=="#":
                    boxgrid[row][col]="."
                    boxgrid[row][empty]="#"
                    empty-=1
        res=[[""]*rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][rows-1-i]=boxgrid[i][j]
        return res
