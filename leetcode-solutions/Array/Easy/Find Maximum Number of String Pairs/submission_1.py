# Problem: Find Maximum Number of String Pairs
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ind=0
        c=0
        for i in words:
            if i[::-1] in words[ind+1::]:
                c+=1
            ind+=1
        return c
