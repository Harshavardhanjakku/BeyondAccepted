# Problem: Find Missing and Repeated Values
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        newl=[j for i in grid for j in i]
        reval=None
        Missval=None
        for i in range(1,len(grid)**2+1):
            if newl.count(i)==0:
                Missval=i
            elif newl.count(i)==2:
                reval=i
            else:
                continue
        return [reval,Missval]
