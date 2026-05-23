# Problem: Find Words Containing Character
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        l=[]
        c=0
        for i in words:
            if x in i:
                l.append(c)
            c+=1
        return l
