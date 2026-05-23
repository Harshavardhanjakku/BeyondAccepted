# Problem: Find Most Frequent Vowel and Consonant
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vdic={}
        cdic={}
        VOWELS="aeiou"
        for i in s:
            if i in VOWELS :
                if i not in vdic :
                    vdic[i]=1
                else:
                    vdic[i]+=1
            else:
                if i not in cdic:
                    cdic[i]=1
                else:
                    cdic[i]+=1
        vmaxi=0
        cmaxi=0
        for i in vdic:
            vmaxi=max(vmaxi,vdic[i])
        for i in cdic:
            cmaxi=max(cmaxi,cdic[i])
        return vmaxi+cmaxi



