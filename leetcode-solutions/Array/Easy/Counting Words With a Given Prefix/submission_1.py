# Problem: Counting Words With a Given Prefix
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        c=0
        n=len(pref)
        for i in words:
            if i[:n:]==pref:
                c+=1
        return c
