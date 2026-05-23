# Problem: Find Words Containing Character
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i in range(len(words)):
            a = words[i]
            if x in a:
                res.append(i)
        return res
 
