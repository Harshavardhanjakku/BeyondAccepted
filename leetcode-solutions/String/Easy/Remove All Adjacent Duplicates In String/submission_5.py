# Problem: Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 5

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if not stack or i!= stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)


