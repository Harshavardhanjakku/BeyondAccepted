# Check if the Sentence Is Pangram
# Difficulty: Easy
# Language: python

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)>=26:
            import string
            mystr=string.ascii_lowercase
            for i in mystr[::-1]:
                if i not in sentence:
                    return False
            return True
        else:
            return False
        
