# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i==")" and stack and stack[-1]=="(":
                stack.pop()
            elif i=="]" and stack and stack[-1]=="[":
                stack.pop()           
            elif i=="}" and stack and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(i)
        return stack==[]
                           
