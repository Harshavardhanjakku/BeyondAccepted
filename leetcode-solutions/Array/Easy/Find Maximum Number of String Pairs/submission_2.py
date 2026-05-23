# Problem: Find Maximum Number of String Pairs
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ind=0
        c=0
        for i in words:
            j=ind+1
            if i[::-1] in words[j::]:
                c+=1
            ind+=1
        return c
