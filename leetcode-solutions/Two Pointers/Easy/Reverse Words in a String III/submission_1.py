# Problem: Reverse Words in a String III
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        ind=0
        s=""
        for i in l:
            s+=i[::-1]+" "
        return s[:-1]
            

        
