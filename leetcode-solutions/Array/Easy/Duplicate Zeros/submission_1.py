# Problem: Duplicate Zeros
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None
        Modify arr in-place using an auxiliary array.
        """
        n=len(arr)
        temp=[0]*n
        i=0
        j=0
        while i<n and j<n:
            temp[j]=arr[i]
            if arr[i]==0 and j+1<n:
                temp[j+1]=0
                j+=1
            i+=1
            j+=1
        arr[:]=temp
