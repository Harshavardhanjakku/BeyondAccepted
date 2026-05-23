# Problem: Replace Elements with Greatest Element on Right Side
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l=[]
        n=len(arr)
        for i in range(n):
            if i==n-1:
                l.append(-1)
            elif i!=0 and arr[i]<l[-1] :
                l.append(l[-1])
            else:
                l.append(max(arr[i+1::]))
        return l
