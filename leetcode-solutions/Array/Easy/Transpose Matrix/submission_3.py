# Problem: Transpose Matrix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tm=[]
        for col in range(len(matrix[0])):
            ml=[]
            for row in range(len(matrix)):
                ml.append(matrix[row][col])
            tm.append(ml)
        return tm
