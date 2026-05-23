# Problem: Transpose Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tm=[]
        m=len(matrix[0])
        n=len(matrix)
        for col in range(m):
            ml=[]
            for row in range(n):
                ml.append(matrix[row][col])
            tm.append(ml)
        return tm
