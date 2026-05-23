# Problem: Maximum Odd Binary Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        no=s.count("1")
        nz=s.count("0")
        if no>0:
            res=(no-1)*"1"+nz*"0"+"1"
        else:
            res=nz*"0"+no*"1"
        return res

