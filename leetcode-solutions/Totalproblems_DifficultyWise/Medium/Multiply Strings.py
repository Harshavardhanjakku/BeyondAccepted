# Multiply Strings
# Difficulty: Medium
# Language: python

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        no1,no2=0,0
        for i in num1:
            no1=no1*10+(ord(i)-48)
        for i in num2:
            no2=no2*10+(ord(i)-48)
        return str(no1*no2)
        
