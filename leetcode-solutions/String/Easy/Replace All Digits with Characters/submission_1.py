# Problem: Replace All Digits with Characters
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import string
        ns=""
        ind=0
        for i in s:
            if i.isnumeric():
                ns+=chr(ord(ns[-1])+int(i))
                ind+=1
            else:
                ns+=i
        return ns
                
