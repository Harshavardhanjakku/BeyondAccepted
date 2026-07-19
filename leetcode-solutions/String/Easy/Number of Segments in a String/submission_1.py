# Problem: Number of Segments in a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
