# Problem: Maximum Substrings With Distinct Start
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 2

class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=list(s)
        return len(set(s))
