# Problem: Merge Strings Alternately
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 2

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m=len(word1)
        n=len(word2)
        l=[]
        i=0
        j=0
        while i<m and j<n:
            l.append(word1[i]+word2[j])
            i+=1
            j+=1
        while i<m:
            l.append(word1[i])
            i+=1
        while j<n:
            l.append(word2[j])
            j+=1
        return "".join(l)

