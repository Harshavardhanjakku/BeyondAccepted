# Reverse Words in a String III
# Difficulty: Easy
# Language: python

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
            

        
