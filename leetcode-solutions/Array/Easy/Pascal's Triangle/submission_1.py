# Problem: Pascal's Triangle
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        import math
        finalres=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(math.comb(i,j))
            finalres.append(temp)
        return finalres
