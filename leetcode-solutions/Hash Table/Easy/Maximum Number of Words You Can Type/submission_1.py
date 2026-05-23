# Problem: Maximum Number of Words You Can Type
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count=0
        text=text.split()
        for x in text:
            z=set(x).intersection(set(brokenLetters)) 
            if len(z)==0:
                count+=1
        return count
