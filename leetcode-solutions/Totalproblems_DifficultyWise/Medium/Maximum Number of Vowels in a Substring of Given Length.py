# Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
# Language: python

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        vc=0
        maxi=0
        vowelset={'a','e','i','o','u'}
        while j<k:
            if s[j] in vowelset:
                vc+=1
            maxi=max(maxi,vc)
            j+=1
        while j<len(s):
            if s[i] in vowelset:
                vc-=1
            if s[j] in vowelset:
                vc+=1
            maxi=max(maxi,vc)
            j+=1
            i+=1
        return maxi
