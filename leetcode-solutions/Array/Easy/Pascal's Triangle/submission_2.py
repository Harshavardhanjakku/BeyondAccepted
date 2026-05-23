# Problem: Pascal's Triangle
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def fact(num):
            if num==0 or num==1:
                return 1
            else:
                return num*fact(num-1)    
        ol=[]
        for i in range(n):
            l=[]
            for j in range(i+1):
                res=fact(i)//(fact(i-j)*fact(j))
                l.append(res)
            ol.append(l)    
        return ol

        
