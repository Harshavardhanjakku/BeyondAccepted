# Problem: Lucky Numbers in a Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rl=[]
        for i in matrix:
            rl.append(min(i))
        row=0
        cl=[]
        for col in range(len(matrix[0])):
            ml=[]
            for row in range(len(matrix)):
                ml.append(matrix[row][col])
            cl.append(max(ml))
        return (list(set(cl)&set(rl)))
        

        
