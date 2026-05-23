# Problem: Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res=[]
        a=set()
        b=set()
        n=len(A)
        for i in range(n):
            a.add(A[i])
            b.add(B[i])
            res.append(len(a&b))
        return res
