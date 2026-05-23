# Problem: Maximum Area of Longest Diagonal Rectangle
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        a,b = max(dimensions, 
                key = lambda x: (x[0]*x[0]+x[1]*x[1], (x[0]*x[1])))

        return a*b
