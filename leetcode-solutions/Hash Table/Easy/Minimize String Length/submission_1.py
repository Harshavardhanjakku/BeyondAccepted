# Problem: Minimize String Length
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
