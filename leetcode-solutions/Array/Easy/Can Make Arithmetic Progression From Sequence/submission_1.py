# Problem: Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        a=min(arr)
        l=max(arr)
        n=len(arr)
        d=(l-a)//(n-1)
        s=set(arr)
        if (l - a) % (n - 1) != 0:
            return False
        for i in range(n):
            if a+(i*d) not in s:
                return False
        return True
