# Problem: Shuffle String
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dic={}
        j=0
        for i in indices:
            dic[i]=s[j]
            j=j+1
        y=''
        for j in range(len(s)):
            y+=dic[j]
        return y
        
