# Problem: Reverse String Prefix
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return s[:k][::-1] + s[k:]

