# Problem: Find Missing and Repeated Values
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)**2
        newl=[j for i in grid for j in i]
        lsum=sum(newl)
        for i in set(newl):
            newl.remove(i)
        rval=newl[0]
        misval=(n*(n+1)//2)+ rval - lsum
        return [rval,misval]
