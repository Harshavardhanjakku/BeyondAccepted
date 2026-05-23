# Problem: Truncate Sentence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.split()
        s=s[:k:]
        return " ".join(s)
