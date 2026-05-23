# Problem: Rotate String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            rotation = s[i:] + s[:i]
            if rotation==goal:
                return True
        return False
