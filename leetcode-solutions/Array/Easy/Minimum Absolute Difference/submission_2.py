# Problem: Minimum Absolute Difference
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        n=len(arr)
        mymin=float('inf')
        for i in range(n-1):
            if arr[i+1]-arr[i]<mymin:
                mymin=arr[i+1]-arr[i]
        return [[arr[i],arr[i+1]] for i in range(n-1) if arr[i+1]-arr[i]==mymin]
