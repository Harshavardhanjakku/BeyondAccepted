# Problem: Duplicate Zeros
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        l=[0]*n
        i=j=0
        while j<n :
            if arr[i]!=0:
                l[j]=arr[i]
                j+=1
            else:
                l[j]=arr[i]
                if j<n-1:
                    l[j+1]=arr[i]
                j+=2
            i+=1
            
        arr[:]=l[:]

        
