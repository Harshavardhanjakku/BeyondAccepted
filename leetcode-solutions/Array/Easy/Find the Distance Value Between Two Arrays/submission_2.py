# Problem: Find the Distance Value Between Two Arrays
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n=noe=len(arr1)
        for i in arr1:
            flag=False
            for j in arr2:
                if abs(j-i)<=d:
                    flag=True
                    break
            if flag:
                noe-=1
        return noe


