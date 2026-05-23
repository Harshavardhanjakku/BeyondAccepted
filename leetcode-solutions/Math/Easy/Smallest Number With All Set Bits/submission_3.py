# Problem: Smallest Number With All Set Bits
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n>0:
            c+=1
            n=n>>1
        return (1<<c)-1
