# Problem: Happy Number
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=set()
        while (True):
            l.add(n)
            i=list(map(int,list(str(n))))
            n=sum([x**2 for x in i])
            if n in l and n!=1:
                return False
            elif n==1:
                return True
            


