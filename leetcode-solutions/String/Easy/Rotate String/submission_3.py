# Problem: Rotate String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        m=len(s)
        n=len(goal)
        if m!=n:
            return False
        return goal in s+s
