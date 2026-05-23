# Problem: Reverse Prefix of Word
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind=word.find(ch)
        if ind==-1:
            return word
        else:
            word=word.replace(word[:ind+1],word[:ind+1][::-1])
            return word
