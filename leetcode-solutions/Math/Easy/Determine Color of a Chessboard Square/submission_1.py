# Problem: Determine Color of a Chessboard Square
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        return True if (ord(coordinates[0])+int(coordinates[1]))%2 else False
