# Problem: Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a=set()
        b=set()
        res=[]
        for  i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            res.append(len(a&b))
        return res




