# Rotate String
# Difficulty: Easy
# Language: python

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
