# Problem: Counting Bits
# Difficulty: Easy
# Topic: Dynamic Programming
# Language: python
# Submission: 1

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(0,n+1):
            temp=i
            mycnt=0
            while temp:
                mycnt+=1
                temp=temp&(temp-1)
            res.append(mycnt)
        return res

