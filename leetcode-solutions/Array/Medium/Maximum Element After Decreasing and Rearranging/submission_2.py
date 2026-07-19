# Problem: Maximum Element After Decreasing and Rearranging
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        curr = arr[0]
        n=len(arr)
        maxi=arr[0]=1
        for i in range(1,n):
            if arr[i]-arr[i-1]>1:
                arr[i]=arr[i-1]+1
            maxi=max(maxi,arr[i])
        return maxi

