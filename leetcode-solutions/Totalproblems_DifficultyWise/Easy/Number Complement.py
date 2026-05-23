# Number Complement
# Difficulty: Easy
# Language: python

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=bin(num)[2:]
        l=list(s)
        for i in range(len(s)):
            if l[i]=='0':
                l[i]='1'
            else:
                l[i]='0'
        return int(''.join(l),2)
        
