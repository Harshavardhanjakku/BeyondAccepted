# Find the Peaks
# Difficulty: Easy
# Language: python

class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(mountain)
        for i in range(1,n-1):
            if mountain[i-1]<mountain[i]>mountain[i+1]:
                res.append(i)
        return res
