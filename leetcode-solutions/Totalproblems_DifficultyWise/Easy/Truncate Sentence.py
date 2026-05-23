# Truncate Sentence
# Difficulty: Easy
# Language: python

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.split()
        return " ".join(s[:k:])
