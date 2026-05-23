# Problem: Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)>2:
            l,a,s,n=max(arr),min(arr),sum(arr),len(arr)
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
