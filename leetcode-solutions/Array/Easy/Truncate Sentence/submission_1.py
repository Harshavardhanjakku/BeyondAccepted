# Problem: Truncate Sentence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.split()
        return " ".join(s[:k:])
