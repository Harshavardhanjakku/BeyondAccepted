# Maximum Odd Binary Number
# Difficulty: Easy
# Language: python

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

