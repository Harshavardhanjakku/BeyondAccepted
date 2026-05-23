# Bitwise AND of Numbers Range
# Difficulty: Medium
# Language: python

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        while right>left:
            right=right&(right-1)
        return right
