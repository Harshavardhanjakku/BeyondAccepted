# Row With Maximum Ones
# Difficulty: Easy
# Language: python

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        onc=[i.count(1) for i in mat]    
        mc=max(onc)
        ind=onc.index(mc)
        return [ind,mc]



