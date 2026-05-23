# Transpose Matrix
# Difficulty: Easy
# Language: python3

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
