# Problem: Reverse Vowels of a String
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 2

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        sl=list(s)
        vs="aeiouAEIOU"
        while i<j:
            if sl[i] not in vs :
                i+=1
            elif sl[j] not in vs :
                j-=1
            else:
                sl[i],sl[j]=sl[j],sl[i]
                i+=1
                j-=1

        return "".join(sl)
