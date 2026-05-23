# Pascal's Triangle II
# Difficulty: Easy
# Language: python

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def fact(no):
            if no==0 or no==1:
                return 1
            else:
                return no*fact(no-1)
        l=[]
        n=rowIndex
        for r in range(n+1):
            nCr=fact(n)/(fact(n-r)*fact(r))
            l.append(nCr)
        return l


        
