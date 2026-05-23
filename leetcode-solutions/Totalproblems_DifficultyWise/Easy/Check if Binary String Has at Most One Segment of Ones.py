# Check if Binary String Has at Most One Segment of Ones
# Difficulty: Easy
# Language: python

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len([x for x in s.split("0") if x])<=1
