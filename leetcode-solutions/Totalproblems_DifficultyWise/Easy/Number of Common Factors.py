# Number of Common Factors
# Difficulty: Easy
# Language: python

class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def hcf(ano,bno):
            if bno%ano==0:
                return ano
            else:
                return hcf(bno%ano,ano)
        res=hcf(a,b) if a<b else hcf(b,a)
        count=0
        for i in range(1,res+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
