# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=="":
            return True
        l=[]
        top=-1
        for i in s:
            if top==-1:
                l.append(i)
                top+=1
            elif i=='}' and l[-1]=='{':
                l.pop()
                top-=1
            elif i==']' and l[-1]=='[':
                l.pop()
                top-=1
            elif i==')' and l[-1]=='(':
                l.pop()
                top-=1
            else:
                l.append(i)
                top+=1
        return True if len(l)==0 else False
