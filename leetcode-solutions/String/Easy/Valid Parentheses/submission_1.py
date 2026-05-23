# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def isValid(self,s):
        stack=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i==")" and stack and stack[-1]=="(":
                stack.pop()
            elif i=="]" and stack and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack and stack[-1]=="{":
                stack.pop()
            else:
                return False
        return stack==[]
