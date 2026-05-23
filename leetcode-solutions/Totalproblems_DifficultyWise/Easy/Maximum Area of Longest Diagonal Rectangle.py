# Maximum Area of Longest Diagonal Rectangle
# Difficulty: Easy
# Language: python3

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        a,b = max(dimensions, 
                key = lambda x: (x[0]*x[0]+x[1]*x[1], (x[0]*x[1])))

        return a*b
