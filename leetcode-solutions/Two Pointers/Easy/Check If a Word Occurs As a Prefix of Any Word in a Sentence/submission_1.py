# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        pos=1
        for i in sentence.split(" "):
            if i.startswith(searchWord):
                return pos 
            pos+=1
        return -1
        
