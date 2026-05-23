# Problem: Rotating the Box
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def rotateTheBox(self, boxgrid):
        """
        :type boxgrid: List[List[str]]
        :rtype: List[List[str]]
        """
        rows=len(boxgrid)
        cols=len(boxgrid[0])
        for row in range(rows):
            count=0
            for col in range(cols):
                if boxgrid[row][col]=="#":
                    count+=1
                    boxgrid[row][col]="."
                elif boxgrid[row][col]=="*":
                    col-=1
                    while count>0:
                        boxgrid[row][col]="#"
                        col-=1
                        count-=1
            col=cols-1
            while count>0:
                boxgrid[row][col]="#"
                col-=1
                count-=1
        res=[[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                res[i][j]=boxgrid[j][i]
        for row in range(cols):
            res[row]=res[row][::-1]
        return res
