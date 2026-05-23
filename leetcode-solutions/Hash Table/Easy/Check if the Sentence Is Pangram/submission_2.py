# Problem: Check if the Sentence Is Pangram
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 2

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)>=26:
            import string
            mystr=string.ascii_lowercase
            for i in mystr:
                if i not in sentence:
                    return False
            return True
        else:
            return False
        
