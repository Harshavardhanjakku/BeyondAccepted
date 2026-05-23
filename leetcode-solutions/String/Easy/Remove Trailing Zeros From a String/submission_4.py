# Problem: Remove Trailing Zeros From a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 4

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        n=int(num)
        while(n>0):
            if n%10!=0:
                break
            else:
                n//=10
        return str(n)
