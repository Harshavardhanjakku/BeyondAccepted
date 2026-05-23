# Problem: Clear Digits
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

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
