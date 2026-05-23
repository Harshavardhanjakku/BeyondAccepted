# Clear Digits
# Difficulty: Easy
# Language: python

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import string
        if s=="":
            return s
        else:
            l=[]
            for i in s:
                if i.isdigit():
                    l.pop()
                else:
                    l.append(i)
            return "".join(l)
