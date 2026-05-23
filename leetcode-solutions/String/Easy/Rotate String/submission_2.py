# Problem: Rotate String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return  len(goal)==len(s) and goal in s+s
