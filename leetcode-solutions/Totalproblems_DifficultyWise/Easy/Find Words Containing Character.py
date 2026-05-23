# Find Words Containing Character
# Difficulty: Easy
# Language: python

class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
 
