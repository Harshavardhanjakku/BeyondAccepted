# Problem: Find Words Containing Character
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indexlis=[]
        for i in range(len(words)):
            if x in words[i]:
                indexlis.append(i)
        return indexlis
        
