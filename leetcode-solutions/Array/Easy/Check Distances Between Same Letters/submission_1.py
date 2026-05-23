# Problem: Check Distances Between Same Letters
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        lis=[0]*26
        myset=set(s)
        for i in myset:
            lis[ord(i)-97]=s.rindex(i)-s.index(i)-1
            if lis[ord(i)-97]!=distance[ord(i)-97]:
                return False
        return True
        
