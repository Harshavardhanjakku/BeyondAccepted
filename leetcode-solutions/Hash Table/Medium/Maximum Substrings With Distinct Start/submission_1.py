# Problem: Maximum Substrings With Distinct Start
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
