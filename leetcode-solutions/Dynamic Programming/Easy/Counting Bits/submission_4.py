# Problem: Counting Bits
# Difficulty: Easy
# Topic: Dynamic Programming
# Language: python
# Submission: 4

class Solution(object):
    def countBits(self, n):
        def checkithbit(a,i):
            return (a>>i)&1 ==1
        ol=[]
        for a in range(n+1):
            c=0
            for i in range(31):
                if checkithbit(a,i):
                    c+=1
            ol.append(c)
        return ol


            
                
