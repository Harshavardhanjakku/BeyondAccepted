# Problem: Ugly Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(True):
            if n>5:
                if n%2==0 :
                    n=n//2
                elif n%3==0 :
                    n=n//3
                elif n%5==0 :
                    n=n//5
                else:
                    return False
            elif n>0 and n<=5:
                return True
            else:
                return False

