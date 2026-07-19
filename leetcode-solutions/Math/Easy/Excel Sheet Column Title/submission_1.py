# Problem: Excel Sheet Column Title
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def convertToTitle(self,c ):
        s=""
        while c > 0:
            c-=1
            s+=chr(65+c%26)
            c=c//26
        return s[::-1]
