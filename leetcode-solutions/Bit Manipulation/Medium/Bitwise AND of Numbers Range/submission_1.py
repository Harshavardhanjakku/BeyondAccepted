# Problem: Bitwise AND of Numbers Range
# Difficulty: Medium
# Topic: Bit Manipulation
# Language: python
# Submission: 1

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        while right>left:
            right=right&(right-1)
        return right
