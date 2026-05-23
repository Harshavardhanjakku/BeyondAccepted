# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 5

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
            elif mystack :
                if  i=="}" and mystack[-1]=="{":
                    mystack.pop()
                elif  i=="]" and mystack[-1]=="[":
                    mystack.pop()
                elif  i==")" and mystack[-1]=="(":
                    mystack.pop()                
                else:
                    return False 
            else:
                return False
        return mystack==[]       
