# Problem: Excel Sheet Column Title
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def convertToTitle(self,columnNumber):
        s=""
        while columnNumber>0:
            columnNumber-=1
            s=chr(65+columnNumber%26)+s
            columnNumber//=26
        return s
