# Find the Pivot Integer
# Difficulty: Easy
# Language: python

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumofn=(n*(n+1))//2
        for i in range(1,n+1):
            s=(i*(i+1))//2
            if s==(sumofn-s+i):
                return i

        return -1
