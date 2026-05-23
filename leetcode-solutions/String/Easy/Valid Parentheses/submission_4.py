# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 4

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack=[]
        for i in s:
            if i=="(" or i=="{" or i=="[" :
                mystack.append(i)
            elif i=="}":
                if  mystack!=[] and mystack[-1]=="{":
                    mystack.pop()
                else:
                    mystack.append(i)
            elif i=="]":
                if mystack!=[] and mystack[-1]=="[":
                    mystack.pop()
                else:
                    mystack.append(i)
            elif i==")":
                if mystack!=[] and mystack[-1]=="(":
                    mystack.pop()
                else:
                    mystack.append(i)   
        return mystack==[]       
