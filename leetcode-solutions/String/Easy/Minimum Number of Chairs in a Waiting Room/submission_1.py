# Problem: Minimum Number of Chairs in a Waiting Room
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        mc=0
        for i in s :
            if i=="E":
                c+=1
            elif i=="L":
                c-=1
            if c>mc:
                mc=c
        return mc
        
            
        
