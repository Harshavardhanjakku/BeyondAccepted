# Problem: Determine Color of a Chessboard Square
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        res=ord(coordinates[0])+int(coordinates[1])
        return True if res%2 else False
