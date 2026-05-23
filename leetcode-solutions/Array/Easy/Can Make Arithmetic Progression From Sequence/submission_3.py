# Problem: Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        if n>2:
            l,a,s=max(arr),min(arr),sum(arr)
            arr.remove(l)
            scmax=max(arr)
            d1=l-scmax
            arr.remove(a)
            scmin=min(arr)
            d2=scmin-a
            if (a+((n-1)*d1)==l) and s==((n)*(a+l)/2) and (d1==d2):
                return True
            else:
                return False
        else:
            return True
