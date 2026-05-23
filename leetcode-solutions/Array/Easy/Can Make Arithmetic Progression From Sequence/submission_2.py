# Problem: Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        n=len(arr)
        d=arr[1]-arr[0]
        flag=True
        for i in range(n-1):
            if arr[i+1]-arr[i]!=d:
                flag=False
        return flag
