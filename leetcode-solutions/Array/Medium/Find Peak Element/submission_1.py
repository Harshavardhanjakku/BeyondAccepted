# Problem: Find Peak Element
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findPeakElement(self, l):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(l)
        i,j=0,n-1
        while i<=j:
            mid=i+(j-i)//2
            if(mid==0 or l[mid]>=l[mid-1])and(mid==n-1 or l[mid]>=l[mid+1]):
                return mid
                break
            elif mid > 0 and l[mid - 1] > l[mid]:
                j = mid - 1
            else:
                i = mid + 1
