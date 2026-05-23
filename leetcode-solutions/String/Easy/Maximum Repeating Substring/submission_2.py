# Problem: Maximum Repeating Substring
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        m=len(word)
        n=len(sequence)
        count=1
        maxi=0
        while count*m<=n:
            if word*count in sequence:
                maxi=count
            count+=1
        return maxi
            

