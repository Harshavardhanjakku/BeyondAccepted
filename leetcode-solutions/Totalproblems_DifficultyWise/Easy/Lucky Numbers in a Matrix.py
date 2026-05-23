# Lucky Numbers in a Matrix
# Difficulty: Easy
# Language: python3

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rl=set()
        for i in matrix:
            rl.add(min(i))
        cl=set()
        for col in range(len(matrix[0])):
            ml=set()
            for row in range(len(matrix)):
                ml.add(matrix[row][col])
            cl.add(max(ml))
        return (cl&rl)
        

        
